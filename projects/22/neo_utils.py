from py2neo import Graph

import config


def execute_query(query):
    graph = connect_to_graph()
    response = graph.run(query)
    return response


def clear_graph():
    graph = connect_to_graph()
    graph.delete_all()


def connect_to_graph():
    graph = Graph(config.neo4j_url, user=config.neo4j_user, password=config.neo4j_password)
    return graph
