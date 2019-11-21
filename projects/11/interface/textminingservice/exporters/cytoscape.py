class CytoscapeSerializer(object):
    @staticmethod
    def serialize(nodes, edges):
        list_of_elements = []
        for node in nodes:
            list_of_elements.append(CytoscapeSerializer.serialize_node(node))
        for edge in edges:
            list_of_elements.append(CytoscapeSerializer.serialize_edge(edge))
        return list_of_elements

    @staticmethod
    def serialize_node(node):
        data_dict = {
            "id": str(node.node_id),
            "uri": node.uri or '',
            "name": node.label,
            "query": True,
            "gene": True
        }
        if node.score:
            data_dict['score'] = node.score
        return {
            "data": data_dict,
            "group": "nodes",
            "removed": False,
            "selected": False,
            "selectable": True,
            "locked": False,
            "grabbable": True,
            "classes": "fn6935"
        }

    @staticmethod
    def serialize_edge(edge):
        return {
            "data": {
                "source": str(edge.source.node_id),
                "target": str(edge.target.node_id),
                "networkId": 1133,
                "networkGroupId": 18,
                "intn": True,
                "id": edge.id
            },
            "position": {},
            "group": "edges",
            "removed": False,
            "selected": False,
            "selectable": True,
            "locked": False,
            "grabbable": True,
            "classes": ""
        }
