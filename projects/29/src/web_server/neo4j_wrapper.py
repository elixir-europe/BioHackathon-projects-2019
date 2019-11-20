import collections
from typing import ValuesView, Dict, Optional, List

import yaml
from neo4j import GraphDatabase

with open('config.yaml') as fd:
    CONFIG = yaml.load(fd)

driver = GraphDatabase.driver(CONFIG['neo4j']['neo4j_endpoint'], auth=(CONFIG['neo4j']['user'], CONFIG['neo4j']['pass']))

def print_node_types(tx):
    return tx.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() RETURN distinct keys(n) AS r")


def print_publications(tx, doi):
    #return tx.run("MATCH (n1 {id: 'http://identifiers.org/doi/10.1101/476457'})-[r]->(n2) RETURN r, n1, n2 LIMIT 25")
    #print("MATCH (n1 {id: " + doi + "})-[r]->(n2) RETURN r, n1, n2 LIMIT 25")
    return tx.run("MATCH (n1 {id: '" + doi + "'})-[r]->(n2) RETURN r, n1, n2 LIMIT 25")
    #return tx.run("MATCH (n1 {id: '$doi'})-[r]->(n2) RETURN r, n1, n2 LIMIT 25", doi=doi)


def print_publications(tx, where):
    #return tx.run("MATCH (n1 {id: 'http://identifiers.org/doi/10.1101/476457'})-[r]->(n2) RETURN r, n1, n2 LIMIT 25")
    #print("MATCH (n1 {id: " + doi + "})-[r]->(n2) RETURN r, n1, n2 LIMIT 25")
    print("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 LIMIT 25")
    return tx.run("MATCH (n1)-[r]->(n2) WHERE " + where + " RETURN r, n1, n2 LIMIT 25")
    #return tx.run("MATCH (n1 {id: '$doi'})-[r]->(n2) RETURN r, n1, n2 LIMIT 25", doi=doi)


def execute_cypher_simple(query):
    with driver.session() as session:
        value = session.read_transaction(print_publications, query)
        #print(list(value.records()))
        #print([record["r"] for record in value.records()])
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
        #print(list(value.records()))
        #print([record["r"] for record in value.records()])
        return {"values": [(record["r"], record["n2"]) for record in value.records()]}
