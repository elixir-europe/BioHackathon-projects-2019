"""Compute pairwise distances between nodes in Neo4J database."""

import numpy as np
import pandas as pd
from scipy.spatial import distance

import seaborn as sns
import matplotlib.pyplot as plt

from neo4j import GraphDatabase


class Neo4jWrapper:
    """
    MATCH (n)
    DETACH DELETE n
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

    def create_relationship(self, node1, node2, prop):
        """Note: must be directed by Neo4j design."""
        cypher_cmd = '''
            MATCH (a:Person), (b:Person)
            WHERE a.name = $node1 AND b.name = $node2
            CREATE (a)-[r:distance { value: $prop }]->(b)
            RETURN type(r), r.name
        '''

        with self._driver.session() as session:
            return session.read_transaction(
                self._exec(cypher_cmd),
                node1=node1, node2=node2, prop=prop
            )


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


if __name__ == '__main__':
    main()
