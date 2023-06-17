from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
from logarithmicEncoding import LogarithmicEncoding
from bracketEncoding import BracketEncoding
from suffixEncoding import SuffixEncoding
from Constants import translate_to_dna, translate_from_dna

# print(translate_from_dna(translate_to_dna("hello world")))

# tree = TriTree(Node("node1", 4), branching_degree=4)
# tree.add_node("node1", ["node2", "node3", "node4", "node8"])
# tree.add_node("node3", ["node5", "node6", "node7", "node9"])

# print(tree.get_tree_string())

t = LogarithmicEncoding(None, initial_value="a(be,c(fg(4,13,4a),h,e),d(1,2,412))",
                        branching_degree=3)
print(t.get_tree_string())
enc = t.tree_to_dna()
print(translate_from_dna(enc, version="log"))
dec = LogarithmicEncoding(None, dna_value=enc)
print(dec.get_tree_string())

# bracket_tree = BracketEncoding(None, initial_value="a(be,c,d(1,2,412))")
# print(bracket_tree.get_tree_string())
# enc = bracket_tree.tree_to_dna()
# print(enc)
# print(translate_from_dna(enc, "bracket"))
# new_bracket = BracketEncoding(None, dna_value=enc)
# print(new_bracket.get_tree_string())

# suffix_tree = SuffixEncoding(None, initial_value="node1(node2,node3(node5,node6(node8,node9,node10),node7),node4)")
# print(suffix_tree.get_tree_string())
# enc = suffix_tree.tree_to_dna()
# print(enc)
# new_bracket = SuffixEncoding(None, dna_value=enc, bracket=suffix_tree.mapping["("])
# print(new_bracket.get_tree_string())


