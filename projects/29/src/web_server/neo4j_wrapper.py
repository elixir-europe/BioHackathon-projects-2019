import collections
from typing import ValuesView, Dict, Optional, List

import yaml
from neo4j import GraphDatabase

with open('config.yaml') as fd:
    CONFIG = yaml.load(fd)

driver = GraphDatabase.driver(CONFIG['neo4j']['neo4j_endpoint'], auth=(CONFIG['neo4j']['user'], CONFIG['neo4j']['pass']))

def print_node_types(tx):
    return tx.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() RETURN distinct keys(n) AS r")


def get_properties():
    with driver.session() as session:
        value = session.read_transaction(print_node_types)
        return {"values": [(record["r"]) for record in value.records()]}

def print_publications_simple(tx, doi):
    return tx.run("MATCH (n1 {doi: '" + doi + "'})-[r]->(n2) RETURN r, n1, n2 ORDER BY r.value DESC LIMIT 25")


def print_publications(tx, where):
    print("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 LIMIT 25")
    return tx.run("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 ORDER BY r.value DESC LIMIT 25")


def print_publications_with_update(doi, score):
    pass #TODO() Awesome weight propagation methods should be implemented!

def execute_cypher_simple(query):
    with driver.session() as session:
        value = session.read_transaction(print_publications_simple, query)
        return {"values": [(record["r"], record["n2"]) for record in value.records()]}

def execute_cypher_update(doi, score):
    with driver.session() as session:
        value = session.read_transaction(print_publications_with_update, doi, score)
        return {"values": [(record["r"], record["n2"]) for record in value.records()]}

def test():
    print(category_builder([{"category":"topic","operator":"==","value":"Query and retrieval"}]))
    print(category_builder([{"expressions":[{"category":"topic","operator":"==","value":"Query and retrieval"}]},{"expressions":[{"expressions":[{"category":"author","operator":"contains","value":"Steffen"}]},{"expressions":[{"category":"year","operator":"!=","value":"2019"}],"conditionType":"AND"}],"conditionType":"AND"}]))

def category_builder(query_array):
    TMP = ""
    for item in query_array:
        if "value" in item:
            value = item["value"] if item["value"].isnumeric() else '"' + item["value"] + '"'
        if "conditionType" in item:
            TMP += " " + item["conditionType"] + " "
        if "operator" in item:
            if item["operator"] == "==":
                operator = "="
                TMP += 'n1.' + item["category"] + ' ' + operator + " " + value
            elif item["operator"] == "!=":
                operator = "!="
                TMP += 'n1.' + item["category"] + ' ' + operator + " " + value
            elif item["operator"] == "contains":
                operator = "CONTAINS"
                TMP += 'n1.' + item["category"] + ' ' + operator + " " + value
            elif item["operator"] == "!contains":
                operator = "CONTAINS"
                TMP += "NOT (" + 'n1.' + item["category"] + ' ' + operator + " " + value + ")"
        if "expressions" in item:
            TMP += "(" + category_builder(item["expressions"]) + ")"
    return TMP


def execute_cypher(query_array):
    with driver.session() as session:
        value = session.read_transaction(print_publications, category_builder(query_array))
        return {"values": [(record["n1"], record["r"], record["n2"]) for record in value.records()]}
