class Edges:
    def __init__(self, edges):
        self.edges = edges

    def get_all(self):
        return self.edges

    def get_edges_by_source(self, source):
        return [edge for edge in self.edges if edge['source'] == source]

    def get_edges_by_target(self, target):
        return [edge for edge in self.edges if edge['target'] == target]