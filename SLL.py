""" SLL list, to search, add, and remove
"""


class SLLNode:  # node for SLL list - data and none (Head ->)
    def __init__(self, node_data):
        self.node_data = node_data
        self.next = None

    def __repr__(self):
        """ return a string output to the console."""
        return "The Node for SLL object is: node_data={}".format(self.node_data)

    def get_node(self):
        """ return the node_data (true, false etc..."""
        return self.node_data

    def set_node(self, new_node_data):
        """ Goal is to replace the old node_data with new_node_data here"""
        return self.node_data

    def get_next_node(self):
        """ want to return (get) the self.next attribute"""
        return self.next

    def set_next_node(self, new_next_node):
        """ declare the new next self"""
        self.next = new_next_node


