from decouple import config
from py2neo import Graph, Node


def execute_query(query):
    graph = connect_to_graph()
    response = graph.run(query)
    return response


def save_samples(samples):
    graph = connect_to_graph()
    for sample in samples:
        save_sample(sample, graph)

    print("Saved " + str(len(samples)) + " samples in neo4j")


def clear_graph():
    graph = connect_to_graph()
    graph.delete_all()


def connect_to_graph():
    graph = Graph(config('neo4j_url'), user=config('neo4j_user'), password=config('neo4j_password'))
    return graph


def save_sample(sample, graph):
    material = get_attribute("characteristics.material.0.text", sample)
    organism = get_attribute("characteristics.organism.0.text", sample)
    project = get_attribute("characteristics.project.0.text", sample)

    merge_statement = ""
    for key, value in sample["characteristics"].items():
        merge_statement += 'a.' + key.replace(" ", "_").replace("-", "_") + '= "' + value[0]["text"] + '", '

    merge_node = "MERGE (a:Sample {accession: '" + sample["accession"] + "'}) " \
                 "SET " + merge_statement[:-2] + " " \
                 "RETURN a"
    graph.run(merge_node)

    if "relationships" in sample:
        for rel in sample["relationships"]:
            target_node = "MERGE (a:Sample {accession: '" + rel["target"] + "'}) RETURN a"
            graph.run(target_node)
            rel_query= "MATCH (source:Sample { accession: '" + rel["source"] + "' }) " \
                       "MATCH (target:Sample { accession: '" + rel["target"] + "' }) " \
                       "MERGE (source)-[r:" + rel["type"].upper().replace(" ", "_") + "]->(target) " \
                       "RETURN source, r, target"
            graph.run(rel_query)


def get_attribute(attribute_path, sample):
    path_segments = attribute_path.split(".")
    segment_data = sample
    for segment in path_segments:
        if isinstance(segment_data, list) and len(segment_data) != 0:
            if len(segment_data) > int(segment):
                segment_data = segment_data[int(segment)]
            else:
                return ""
        elif segment in segment_data:
            segment_data = segment_data[segment]
        else:
            return ""

    return segment_data
