"""Compute pairwise distances between nodes in Neo4J database.

Neo4j cheatsheet:
    * List all nodes:
        MATCH (n) RETURN n, properties(n)

    * Delete all nodes and relationships:
        MATCH (n) DETACH DELETE n

    * Delete only relationships:
        MATCH ()-[r]->() DELETE r
"""

import sys

import numpy as np
import pandas as pd
from scipy.spatial import distance

import category_encoders as ce

import seaborn as sns
import matplotlib.pyplot as plt

import sh
from loguru import logger


def analyze_data(df):
    # concept counts per paper
    plt.figure(figsize=(8, 6))
    sns.distplot(df.groupby('id:ID').count()['value'], kde=False)
    plt.xlabel('Concept Count per Paper')
    plt.ylabel('Count')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('concept_per_paper_counts.pdf')


def analyze_distances(df_dists):
    # subset data randomly
    sub_idx = np.random.randint(
        0, df_dists.index.size,
        size=1000)
    df_sub = df_dists.iloc[sub_idx, sub_idx]

    # distance distribution
    plt.figure(figsize=(8, 6))
    sns.distplot(np.random.choice(
        df_dists.values.ravel(),
        1_000_000
    ), kde=False)
    plt.xlabel('Distance')
    plt.ylabel('Count')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('distance_distribution.pdf')

    # cluster papers
    g = sns.clustermap(df_sub, rasterized=True)
    g.savefig('paper_clusters.pdf')


def main(fname_in, fname_out):
    # read data
    logger.info('Read data')
    df = pd.read_csv(fname_in)
    # df.drop_duplicates(inplace=True)

    concept_variables = [
        'containsData:string',
        'containsOperation:string',
        'containsDataFormat:string',
        'hasTopic:string'
    ]
    df = df[df['variable'].isin(concept_variables)]

    # df = df.iloc[:10]

    # encode features
    logger.info('Encode features')
    ohe = ce.OneHotEncoder(handle_unknown='error', use_cat_names=True)

    df_trans = (ohe.fit_transform(df.set_index('id:ID')['value'])
                   .reset_index()
                   .groupby('id:ID')
                   .sum())

    # compute distances
    logger.info('Compute distances')
    df_dists = pd.DataFrame(
        distance.squareform(distance.pdist(
            df_trans,
            metric='jaccard')),
        columns=df_trans.index,
        index=df_trans.index)

    analyze_distances(df_dists)

    # extract relationships
    logger.info('Extract relationships')
    keep = (np.triu(np.ones(df_dists.shape), k=1)
              .astype('bool')
              .reshape(df_dists.size))
    tmp = df_dists.stack()[keep]

    tmp.index.rename([':START_ID', ':END_ID'], inplace=True)
    tmp.name = 'value:FLOAT'

    df_edges = tmp.reset_index()
    df_edges[':TYPE'] = 'distance'

    df_edges[df_edges['value:FLOAT'] < 1]

    df_edges.to_csv(fname_out, index=False)

    # recreate Neo4j database
    logger.info('Recreate Neo4j database')

    node_file = 'node_tmp.csv'
    (df['id:ID'].drop_duplicates()
                .to_frame()
                .to_csv(node_file, index=False))

    sh.neo4j('stop')
    sh.rm('-rf', '/usr/local/var/neo4j/')  # reset database

    sh.Command('neo4j-admin')(
        'import',
        '--mode=csv',
        '--nodes', node_file,
        '--relationships', fname_out,
        _out=sys.stdout, _err=sys.stderr)

    sh.neo4j('start')
    logger.info('Done')


if __name__ == '__main__':
    main('node_file.csv', 'edge_file.csv')
