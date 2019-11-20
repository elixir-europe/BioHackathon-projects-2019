from decouple import config
from py2neo import Graph


def execute_query(query):
    graph = connect_to_graph()
    response = graph.run(query)
    return response


def save_samples(samples):
    graph = connect_to_graph()
    for sample in samples:
        print("saving to graph")
        # todo save to graph


def clear_graph():
    graph = connect_to_graph()
    graph.delete_all()


def connect_to_graph():
    graph = Graph(config('neo4j_url'), user=config('neo4j_user'), password=config('neo4j_password'))
    return graph
