from encodings.tree import TriTree
from encodings.tree import Node
from encodings.specialEncodings.logarithmicEncoding import LogarithmicEncoding
from encodings.specialEncodings.bracketEncoding import BracketEncoding
from encodings.specialEncodings.improvedBracketEncoding import ImprovedBracketEncoding
from helperFunctions.AlphabetFunctions import translate_from_dna, initialize_alphabet


initialize_alphabet(["A", "C", "T", "G"])

tree = TriTree(Node("node1", 4), branching_degree=4)
tree.add_node("node1", ["node2", "node3", "node4", "node8"])
tree.add_node("node3", ["node5", "node6", "node7", "node9"])

print(tree.get_tree_string())

t = LogarithmicEncoding(None, initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(t.get_tree_string())
enc = t.tree_to_dna()
print(translate_from_dna(enc, version="log"))
dec = LogarithmicEncoding(None, dna_value=enc)
print(dec.get_tree_string())

bracket_tree = BracketEncoding(None, initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(bracket_tree.get_tree_string())
enc = bracket_tree.tree_to_dna()
print(enc)
print(translate_from_dna(enc, "bracket"))
new_bracket = BracketEncoding(None, dna_value=enc)
print(new_bracket.get_tree_string())

bracket_tree = ImprovedBracketEncoding(None, initial_value="a(be,c(fg(4,13,4a),h(i,j,k),e),d(1,2,412))")
print(bracket_tree.get_tree_string())
enc = bracket_tree.tree_to_dna()
print(enc)
print(translate_from_dna(enc, "bracket_improved"))
new_bracket = ImprovedBracketEncoding(None, dna_value=enc)
print(new_bracket.get_tree_string())


