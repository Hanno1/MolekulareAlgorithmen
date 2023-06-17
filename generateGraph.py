import string
from itertools import product
from tree import TriTree, Node


def generate_node_names():
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
    g = generate_node_names()

    root = Node(next(g), degree)
    t = TriTree(root, branching_degree=degree)

    generate_rek(t, g, node_count, 1, degree, [root], mode)
    print(t.get_tree_string())


def generate_rek(tree, gen, node_count, current_node_count, degree, current_nodes, mode):
    while current_node_count < node_count:
        if len(current_nodes) == 0:
            if len(current_nodes) == 0:
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
