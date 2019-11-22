class Node:
    def __init__(self, node_id, label, uri=None, score=None):
        self.uri = uri
        self.label = label
        self.node_id = node_id
        self.score = score


class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    @property
    def id(self):
        return "{}-{}".format(self.source.node_id, self.target.node_id)
