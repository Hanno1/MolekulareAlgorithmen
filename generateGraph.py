import string
from itertools import product
from tree import TriTree, Node


def generate_node_names():
    """
    Generator function that returns unique names containing lower case letters and digits
    """
    all_chars = []
    for s in string.ascii_lowercase:
        all_chars.append(s)
    for s in string.digits:
        all_chars.append(s)
    length = 1
    while True:
        arr = ["".join(i) for i in product(all_chars, repeat=length)]
        for i in range(len(arr)):
            yield arr[i]
        length += 1


def generate_tree(node_count, degree, mode="b"):
    """
    generate tree and returns string for the tree

    :param node_count: count of nodes
    :param degree: degree of node, will be 3 normally
    :param mode: is either b or d - b means breadth tree and d depth tree
    :return:
    """
    g = generate_node_names()

    root = Node(next(g), degree)
    t = TriTree(root, branching_degree=degree)

    generate_it(t, g, node_count, 1, degree, [root], mode)
    return t.get_tree_string()


def generate_it(tree, gen, node_count, current_node_count, degree, current_nodes, mode):
    """
    iterative Function to create the actual tree from initial tree tree

    :param tree: initial tree
    :param gen: generator for creating names
    :param node_count: maximum number of nodes
    :param current_node_count: current number of nodes
    :param degree: degree of the tree, normally just 3
    :param current_nodes: nodes there to append new nodes
    :param mode: b or d
    """
    while current_node_count < node_count:
        if len(current_nodes) == 0:
            if len(current_nodes) == 0:
                print("Empty Graph")
                raise ValueError
        if mode == "b":
            parent = current_nodes.pop(0)
        else:
            parent = current_nodes.pop(-1)
        children = []
        for _ in range(degree):
            child = Node(next(gen), degree)
            current_nodes.append(child)
            children.append(child.name)

            current_node_count += 1
        tree.add_node(parent.name, children)
