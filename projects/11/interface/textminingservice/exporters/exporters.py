import json
from typing import List

from textminingservice.exporters.cytoscape import CytoscapeSerializer
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.graph import Node, Edge
from textminingservice.models.publication import Publication


def export_mentions_cytoscape(entities: List[str], publications: List[Publication]) -> str:
    nodes, edges = build_mentions_graph(entities, publications)
    return json.dumps(CytoscapeSerializer.serialize(nodes, edges))


def build_aggregated_mentions_graph(entities, results):
    nodes = []
    edges = []
    # central node
    source_node = Node(0, ", ".join(entities))
    nodes.append(source_node)
    # build nodes and edges for each publication
    for index, publication_dict in enumerate(results, 1):
        target_node = Node(index, publication_dict['info']['id'], publication_dict['info'].get('uri'),
                           publication_dict['score'])
        nodes.append(target_node)
        edges.append(Edge(source_node, target_node))
    return nodes, edges


def export_aggregated_mentions_cytoscape(entities, results):
    nodes, edges = build_aggregated_mentions_graph(entities, results)
    return CytoscapeSerializer.serialize(nodes, edges)


def export_cooccurrences_cytoscape(entity: str, cooccurrences: List[CoOccurrence]):
    nodes, edges = build_cooccurrences_graph(entity, cooccurrences)
    return json.dumps(CytoscapeSerializer.serialize(nodes, edges))


def build_mentions_graph(entities, publications):
    nodes = []
    edges = []
    # central node
    source_node = Node(0, ", ".join(entities))
    nodes.append(source_node)
    # build nodes and edges for each publication
    for index, publication in enumerate(publications, 1):
        target_node = Node(index, publication.id, publication.uri)
        nodes.append(target_node)
        edges.append(Edge(source_node, target_node))
    return nodes, edges


def build_cooccurrences_graph(entity, cooccurrences: List[CoOccurrence]):
    nodes = []
    edges = []
    # central node
    source_node = Node(0, entity)
    nodes.append(source_node)
    # build nodes and edges for each cooccurrence
    for index, cooccurrence in enumerate(cooccurrences, 1):
        target_node = Node(index, cooccurrence.entity, score=index)
        nodes.append(target_node)
        edges.append(Edge(source_node, target_node))
    return nodes, edges
