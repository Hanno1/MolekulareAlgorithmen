from tree_parser import parse_string
import CustomExceptions
from tree import TriTree
import math
from itertools import product
import tree_parser as Tp
from tree import Node
from dna_coded_tree import TrivialEncoding

# tree = TriTree(Node("node1"))
# tree.add_node("node1", ["node2", "node3", "node4"])
# tree.add_node("node3", ["node5", "node6", "node7"])

# print(tree.print_tree())


t = TrivialEncoding(None, "node1(node2,node3(node5,node6,node7),node4)")
enc = t.encode_tree()
new = TrivialEncoding(None, dna_value=enc, bracket=t.mapping["("])
print(new.print_tree())

