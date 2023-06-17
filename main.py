from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
from logarithmicEncoding import LogarithmicEncoding


tree = TriTree(Node("node1", 4), branching_degree=4)
tree.add_node("node1", ["node2", "node3", "node4", "node8"])
tree.add_node("node3", ["node5", "node6", "node7", "node9"])

print(tree.get_tree_string())

t = LogarithmicEncoding(None, initial_value="node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)",
                        branching_degree=3)
print(t.get_tree_string())
enc = t.encode_tree()
print(enc)

new = LogarithmicEncoding(None, dna_value=enc, bracket=t.mapping["("])
print(new.get_tree_string())

