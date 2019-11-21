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

import umap
import category_encoders as ce

import seaborn as sns
import matplotlib.pyplot as plt

import sh
from tqdm import tqdm
from loguru import logger


sns.set_context('talk')


def analyze_results(
    df, df_trans, df_dists,
    umap_highlight=False
):
    ## raw data
    # concept counts per paper
    plt.figure(figsize=(8, 6))
    sns.distplot(df.groupby('id:ID').count()['value'], kde=False)
    plt.xlabel('Concept Count per Paper')
    plt.ylabel('Count')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('concept_per_paper_counts.pdf')

    ## transformed data
    # highlight certain DOIs
    query_doi = 'xxx'
    wave_dois = [
        ['yyy', 'zzz'],
        ['111', '222']
    ]

    # umap
    reducer = umap.UMAP(metric='jaccard')

    embedding = reducer.fit_transform(df_trans)
    df_emb = pd.DataFrame(embedding, index=df_trans.index)

    df_emb['color'] = 'all'
    if umap_highlight:
        df_emb['color'] = 'all'
        for i, wave_dois in enumerate(wave_dois):
            wave_dois = [f'http://identifiers.org/doi/{x}' for x in wave_dois]

            df_emb.loc[wave_dois, 'color'] = f'wave_{i+1:02}'

        df_emb.loc[f'http://identifiers.org/doi/{query_doi}', 'color'] = 'query'

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=0, y=1, hue='color', data=df_emb)
    plt.xlabel('')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('umap.pdf')

    ## distances
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


def main(fname_in):
    neo4j_nodefile = 'neo4j_nodes.csv'
    neo4j_edgefile = 'neo4j_edges.csv'

    # read data
    logger.info('Read data')
    df = pd.read_csv(fname_in, sep='\t')
    # df.drop_duplicates(inplace=True)

    concept_variables = {
        'containsData:string',
        'containsOperation:string',
        'containsDataFormat:string',
        'hasTopic:string'
    }

    # save Neo4j compatible node list (including properties)
    node_properties = (
        df.groupby(['id:ID', 'variable'])
          .apply(lambda x: '|'.join([str(val) for val in x['value'].tolist()]))
          .reset_index()
          .pivot(index='id:ID', columns='variable', values=0)
          .reset_index())

    (df['id:ID'].drop_duplicates()
                .to_frame()
                .merge(node_properties, on='id:ID')
                .to_csv(neo4j_nodefile, index=False))

    # only consider concepts for distance calculations
    df = df[df['variable'].isin(concept_variables)]

    # df = df.sample(1_000)

    # only consider papers with enough concepts
    doi_selection = (df.groupby('id:ID')
                       .count()['value']
                       .to_frame()
                       .query('value >= 1')
                       .index)
    df = df[df['id:ID'].isin(doi_selection)]

    # encode features
    logger.info(f'Encode features (raw-shape: {df.shape})')
    ohe = ce.OneHotEncoder(handle_unknown='error', use_cat_names=True)

    df_trans = (ohe.fit_transform(df.set_index('id:ID')['value'])
                   .reset_index()
                   .groupby('id:ID')
                   .sum())

    weights = 1 / df_trans.sum(axis=0)

    # compute distances
    logger.info(f'Compute distances (trans-shape: {df_trans.shape})')

    dists = distance.pdist(
        df_trans,
        metric='jaccard') #, w=weights

    df_dists = pd.DataFrame(
        distance.squareform(dists),
        columns=df_trans.index,
        index=df_trans.index)

    # convert distance to similarity
    dists = 1 - dists

    df_dists = 1 - df_dists
    np.fill_diagonal(df_dists.values, 1)

    # analyze results
    analyze_results(df, df_trans, df_dists)

    # extract relationships
    logger.info(f'Extract relationships (dists-shape: {df_dists.shape})')

    idx_trans = df_trans.index
    triu_i, triu_j = np.triu_indices(df_trans.shape[0], k=1)

    edge_count = 0
    with open(neo4j_edgefile, 'w') as fd:
        fd.write(':START_ID,:END_ID,:TYPE,value:FLOAT\n')

        for i, j, d in tqdm(zip(triu_i, triu_j, dists), total=len(dists)):
            if d > 0:
                fd.write(f'{idx_trans[i]},{idx_trans[j]},similarity,{d}\n')
                edge_count += 1

    # recreate Neo4j database
    logger.info(f'Recreate Neo4j database (edge-count: {edge_count})')

    sh.neo4j('stop')
    sh.rm('-rf', '/usr/local/var/neo4j/')  # reset database

    sh.Command('neo4j-admin')(
        'import',
        '--mode=csv',
        '--nodes', neo4j_nodefile,
        '--relationships', neo4j_edgefile,
        _out=sys.stdout, _err=sys.stderr)

    sh.neo4j('start')
    logger.info('Done')


if __name__ == '__main__':
    main('node_file.tsv')
