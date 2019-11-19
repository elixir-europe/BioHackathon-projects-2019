import collections
from typing import ValuesView, Dict, Optional, List

import yaml
from neo4j import GraphDatabase

with open('config.yaml') as fd:
    CONFIG = yaml.load(fd)

driver = GraphDatabase.driver(CONFIG['neo4j']['neo4j_endpoint'], auth=(CONFIG['neo4j']['user'], CONFIG['neo4j']['pass']))


def print_publications(tx, doi):
    return tx.run("MATCH (n1)-[r]->(n2) RETURN r, n1, n2 LIMIT 25", doi=doi)

def execute_query(query):
    with driver.session() as session:
        value = session.read_transaction(print_publications, query)
        return {"value": [record["r"] for record in value]}