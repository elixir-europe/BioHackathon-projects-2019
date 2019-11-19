from py2neo import Graph

import config


def main():
    clear_graph()

    sample = config.example_sample
    load_sample_to_neo4j(sample)


def load_sample_to_neo4j(sample):
    graph = connect_to_graph()
    merge_node = "MERGE (a:Sample {accession: '" + sample["accession"] + "'}) RETURN a"
    graph.run(merge_node)

    merge_sample = "MERGE (keanu:Person { name: 'Keanu Reeves' }) " \
                   "ON CREATE SET keanu.created = timestamp() " \
                   "RETURN keanu.name, keanu.created"

    if "relationships" in sample:
        for rel in sample["relationships"]:
            rel_node = "MERGE (a:Sample {accession: '" + rel["target"] + "'}) RETURN a"
            graph.run(rel_node)
            rel_query= "MATCH (source:Sample { accession: '" + rel["source"] + "' }), " \
                              "(target:Sample { accession: '" + rel["target"] + "' }) " \
                       "MERGE (source)-[r:DERIVED_FROM]->(target) " \
                       "RETURN source, r, target"
            graph.run(rel_query)
# config.relationships[rel["type"]]



def clear_graph():
    graph = connect_to_graph()
    graph.delete_all()


def connect_to_graph():
    graph = Graph(config.neo4j_url, user=config.neo4j_user, password=config.neo4j_password)
    return graph


if __name__ == "__main__":
    main()

