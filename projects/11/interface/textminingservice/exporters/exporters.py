import json
from typing import List

from textminingservice.exporters.cytoscape import CytoscapeSerializer
from textminingservice.models.graph import Node, Edge
from textminingservice.models.publication import Publication


def export_mentions_cytoscape(entities: List[str], publications: List[Publication]) -> str:
    nodes, edges = build_mentions_graph(entities, publications)
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
