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


def print_publications(tx, where, limit=9):
    print("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 LIMIT 9")
    return tx.run("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 ORDER BY n2.centrality DESC LIMIT " + str(limit))

def print_publications_with_update(tx, doi):
    print("[" + ",".join(['"' + item + '"' for item in doi.positive]) + "]")
    print("[" + ",".join(['"' + item + '"' for item in doi.negative]) + "]")
    negatives = "[" + ",".join(['"' + item + '"' for item in doi.negative]) + "]"
    positives = "[" + ",".join(['"' + item + '"' for item in doi.positive]) + "]"
    unvoted = "[" + ",".join(['"' + item + '"' for item in doi.unvoted]) + "]"
    print("MATCH (n1)-[r1]-(n2)-[r2]-(n3) WHERE n1.doi IN " + negatives + " AND n3.doi IN" + negatives + " WITH collect(distinct(n2.doi)) + collect(distinct(n3.doi)) as removeList MATCH (n0)-[r]-(n) WHERE n0.doi IN " + positives + " AND (NOT n.doi IN removeList) AND (NOT n.doi IN " + unvoted + " ) RETURN n as n2")
    return tx.run("MATCH (n1)-[r1]-(n2)-[r2]-(n3) WHERE n1.doi IN " + negatives + " AND n3.doi IN " + negatives + " WITH collect(distinct(n2.doi)) + collect(distinct(n3.doi)) as removeList MATCH (n0)-[r]-(n) WHERE n0.doi IN " + positives + " AND (NOT n.doi IN removeList) AND (NOT n.doi IN " + unvoted + " ) AND (NOT n.doi IN " + positives + " ) RETURN n as n2"
    )
    #return tx.run("MATCH (n1)-[r1]-(n2)-[r2]-(n3) WHERE n1.doi IN $negatives AND n3.doi IN $negatives WITH collect(distinct(n2.doi)) + collect(distinct(n3.doi)) as removeList MATCH (n0)-[r]-(n) WHERE n0.doi IN $positives AND (NOT n.doi IN removeList) AND (NOT n.doi IN $unvoted) RETURN n as n2", negatives="[" + ",".join(['"' + item + '"' for item in doi.negative]) + "]", positives="[" + ",".join(['"' + item + '"' for item in doi.positive]) + "]", unvoted= "[" + ",".join(['"' + item + '"' for item in doi.unvoted]) + "]")

def execute_cypher_simple(query):
    with driver.session() as session:
        value = session.read_transaction(print_publications_simple, query)
        return {"values": [record["n2"] for record in value.records()]}

def execute_cypher_update(doi):
    with driver.session() as session:
        value = session.read_transaction(print_publications_with_update, doi)
        return {"values": [record["n2"] for record in value.records()]}

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


def execute_cypher(query_array, limit):
    with driver.session() as session:
        value = session.read_transaction(print_publications, category_builder(query_array), limit)
        return {"values": [record["n2"] for record in value.records()]}
