from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    else:
        if value < node.value:
            node.left = insert(node.left, value)
        else:
            node.right = insert(node.right, value)
    return node


def add_nodes_to_graph(dot, node, parent=""):
    dot.node(str(id(node)), str(node.value))
    if parent != "":
        dot.edge(parent, str(id(node)))
    if node.left:
        add_nodes_to_graph(dot, node.left, str(id(node)))
    if node.right:
        add_nodes_to_graph(dot, node.right, str(id(node)))


def draw_binary_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    dot = Digraph()
    add_nodes_to_graph(dot, root)
    # Change to True if you want to open the image automatically
    dot.render(
        "binary_tree", view=True
    )  # Change to True if you want to open the image automatically


# Example usage:
values = [15, 10, 20, 8, 12, 18, 25]
draw_binary_tree(values)
