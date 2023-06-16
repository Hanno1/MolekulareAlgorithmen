import CustomExceptions
from tree import TriTree
import math
from itertools import product
import tree_parser as Tp
from tree import Node
from dna_coded_tree import TrivialEncoding

tree = TriTree(Node("node1"))
tree.add_node("node1", ["node2", "node3", "node4"])
tree.add_node("node3", ["node5", "node6", "node7"])

print(tree.get_tree_string())

t = TrivialEncoding(None, "node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)")
print(t.get_tree_string())
enc = t.encode_tree()
print(enc)
new = TrivialEncoding(None, dna_value=enc, bracket=t.mapping["("])
print(new.get_tree_string())

