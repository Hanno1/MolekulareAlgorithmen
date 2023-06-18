from tree import TriTree
from tree import Node
from DNA_Encoder import DNA_Encoder
from AlphabetFunctions import translate_from_dna, initialize_alphabet


initialize_alphabet(["A", "C", "T", "G"])

tree = TriTree(Node("node1", 4), branching_degree=4)
tree.add_node("node1", ["node2", "node3", "node4", "node8"])
tree.add_node("node3", ["node5", "node6", "node7", "node9"])

print(tree.get_tree_string())

t = DNA_Encoder(None, version="log", initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(t.get_tree_string())
enc = t.tree_to_dna()
print(translate_from_dna(enc, version="log"))
dec = DNA_Encoder(None, version="log", dna_value=enc)
print(dec.get_tree_string())

bracket_tree = DNA_Encoder(None, version="bracket", initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(bracket_tree.get_tree_string())
enc = bracket_tree.tree_to_dna()
print(enc)
print(translate_from_dna(enc, "bracket"))
new_bracket = DNA_Encoder(None, version="bracket", dna_value=enc)
print(new_bracket.get_tree_string())

bracket_tree = DNA_Encoder(None, version="bracket_improved", initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(bracket_tree.get_tree_string())
enc = bracket_tree.tree_to_dna()
print(enc)
print(translate_from_dna(enc, "bracket_improved"))
new_bracket = DNA_Encoder(None, version="bracket_improved", dna_value=enc)
print(new_bracket.get_tree_string())


