"""Compute pairwise distances between nodes in Neo4J database."""

import numpy as np
import pandas as pd
from scipy.spatial import distance

import seaborn as sns
import matplotlib.pyplot as plt

from neo4j import GraphDatabase


class Neo4jWrapper:
    """ Wrapper for Neo4j.

    Delete all nodes and relationships:
        MATCH (n) DETACH DELETE n

    Delete only relationships:
        MATCH ()-[r]->() DELETE r
    """
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    @staticmethod
    def _exec(cypher_cmd):
        """Return transaction function for given Cypher command."""
        return lambda tx, **kwargs: tx.run(
            cypher_cmd, **kwargs
        ).value()

    def get_nodes(self):
        cypher_cmd = 'MATCH (n) RETURN n, properties(n)'
        with self._driver.session() as session:
            return session.read_transaction(self._exec(cypher_cmd))

    def create_relationships(
        self, doi_list1, doi_list2, prop_list
    ):
        """Note: must be directed by Neo4j design."""
        # sanity checks
        assert len(doi_list1) == len(doi_list2) == len(prop_list)

        # prepare query statement
        cypher_cmd = """
            MATCH (a:AcademicArticle), (b:AcademicArticle)
            WHERE a.doi = $doi1 AND b.doi = $doi2
            CREATE (a)-[r:distance { value: $prop }]->(b)
            RETURN type(r), r.value
        """

        # conduct transactions
        res_list = []
        with self._driver.session() as session:
            for doi1, doi2, prop in zip(doi_list1, doi_list2, prop_list):
                res = session.read_transaction(
                    self._exec(cypher_cmd),
                    doi1=doi1, doi2=doi2, prop=prop
                )
                res_list.append(res)
        return res_list


def compute_distances(nodes):
    """Compute pairwise distances between all nodes."""
    concept_keys = [
        'hasTopic',
        'containsOperation',
        'containsDataFormat',
        'containsData'
    ]
    all_concepts = list({x
                         for n in nodes
                         for key in concept_keys
                         for x in n[key].split('|')})
    mat = np.zeros(shape=(len(nodes), len(all_concepts)))

    # compute feature vectors
    for i, n in enumerate(nodes):
        cur_concepts = [x
                        for key in concept_keys
                        for x in n[key].split('|')]
        for x in cur_concepts:
            mat[i, all_concepts.index(x)] = 1
    df_mat = pd.DataFrame(
        mat,
        columns=all_concepts,
        index=[n['doi'] for n in nodes]
    )

    # compute distances
    dists = distance.squareform(distance.pdist(
        df_mat,
        metric='jaccard'
    ))
    df_dists = pd.DataFrame(
        dists,
        columns=df_mat.index,
        index=df_mat.index
    )

    return df_dists


def analyze_distances(nodes, df_dists):
    # analyse results
    sub_idx = np.random.randint(
        0, df_dists.index.size,
        size=1000)
    df_sub = df_dists.iloc[sub_idx, sub_idx]

    g = sns.clustermap(df_sub, rasterized=True)
    g.savefig('distances.pdf')

    # df.idxmin(axis=0)
    # tmp = {n['doi']: n for n in nodes}


def main():
    wrapper = Neo4jWrapper(xxx)

    # compute all pairwise node distances
    nodes = wrapper.get_nodes()
    df_dists = compute_distances(nodes)

    # analyze results
    analyze_distances(nodes, df_dists)

    # add edges back to Neo4j network
    doi_list1 = []
    doi_list2 = []
    prop_list = []
    for i, j in zip(*np.triu_indices_from(df_dists, k=1)):
        dist = df_dists.iloc[i, j]
        if dist == 1:
            continue

        doi_list1.append(df_dists.index[i])
        doi_list2.append(df_dists.index[j])
        prop_list.append(dist)

    print(f'Adding {len(prop_list)} edges')
    wrapper.create_relationships(
        doi_list1, doi_list2,
        prop_list
    )


if __name__ == '__main__':
    main()
