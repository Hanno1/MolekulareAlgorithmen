from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
from logarithmicEncoding import LogarithmicEncoding
from bracketEncoding import BracketEncoding
from suffixEncoding import SuffixEncoding


"""tree = TriTree(Node("node1", 4), branching_degree=4)
tree.add_node("node1", ["node2", "node3", "node4", "node8"])
tree.add_node("node3", ["node5", "node6", "node7", "node9"])

print(tree.get_tree_string())

t = LogarithmicEncoding(None, initial_value="node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)",
                        branching_degree=3, symbols=["A", "B"])
print(t.get_tree_string())
enc = t.tree_to_dna()
print(enc)

new = LogarithmicEncoding(None, dna_value=enc, bracket=t.mapping["("])
print(new.get_tree_string())"""

# bracket_tree = BracketEncoding(None, initial_value="node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)")
# print(bracket_tree.get_tree_string())
# enc = bracket_tree.tree_to_dna()
# print(enc)
# new_bracket = BracketEncoding(None, dna_value=enc, bracket=bracket_tree.mapping["("])
# print(new_bracket.get_tree_string())

suffix_tree = SuffixEncoding(None, initial_value="node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)")
print(suffix_tree.get_tree_string())
enc = suffix_tree.tree_to_dna()
print(enc)
new_bracket = SuffixEncoding(None, dna_value=enc, bracket=suffix_tree.mapping["("])
print(new_bracket.get_tree_string())
