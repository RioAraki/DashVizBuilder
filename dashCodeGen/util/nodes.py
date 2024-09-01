class Nodes:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_all(self):
        return self.nodes

    def get_nodes_by_type(self, type):
        return [node for node in self.nodes if node['type'] == type]

    def get_node_by_id(self, id):
        # bad implementation, use dictionary in the first place
        return  [node for node in self.nodes if node['id'] == id][0]