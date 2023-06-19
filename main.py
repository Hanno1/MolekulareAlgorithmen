from tree import TriTree
from tree import Node
from DNA_Encoder import DNA_Encoder
from AlphabetFunctions import initialize_alphabet

# Using this function, we save all alphabets for different modes in the Constants file
initialize_alphabet(["A", "C", "T", "G"])

# Testing the regular trinary tree
tree = TriTree(Node("a", degree=3), branching_degree=3)
tree.add_node("a", ["b", "c", "d"])
tree.add_node("c", ["e", "f", "g"])
tree_string = tree.get_tree_string()
print("\nRegular trinary tree initalized with root node and by adding children:",tree.get_tree_string())
tree = TriTree(initial_value=tree_string, branching_degree=3)
print("Regular trinary tree initalized with tree string:",tree.get_tree_string())
tree.initialize_with_string("a1(b2(h8,i9,j10(k11,l12,m13)),c3,d4(e5,f6,g7))")
print("Regular trinary tree initalized with tree string:",tree.get_tree_string())

# We also support n-ary trees
tree = TriTree(initial_value="a(b,c(f,g,h,i),d,e)", branching_degree=4)
print("4-nary tree initalized with tree string:",tree.get_tree_string(),"\n")

# Testing all DNA Encodings and Decodings
tree_string = "a1(b2(h8,i9,j10(k11,l12,m13)),c3,d4(e5,f6,g7))"
print(f"Testing all DNA-Encoding Algorithms using the tree {tree_string}:")
for version in ["log", "bracket", "bracket_improved", "bracket_improved2"]:
    print(f"\tTesting the {version} algorithm:")
    tree = DNA_Encoder(version=version, initial_value=tree_string)
    enc = tree.tree_to_dna()
    print(f"\t\tDNA-encoded tree: {enc}")
    tree = DNA_Encoder(version=version, dna_value=enc)
    print(f"\t\tDNA-decoded tree: {tree.get_tree_string()}")
