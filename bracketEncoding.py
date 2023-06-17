from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
from Constants import translate_from_dna, translate_to_dna


class BracketEncoding(TriTree):
    def __init__(self, root, initial_value=None, dna_value=None, branching_degree=3):
        self.version = "bracket"
        self.branching_degree = branching_degree
        self.names = []
        if initial_value:
            super().__init__(root, initial_value, branching_degree=branching_degree)
        elif dna_value:
            self.root = self.tree_from_dna(dna_value)
        elif root:
            super().__init__(root)

    def tree_to_dna(self):
        return self._tree_to_dna_rek(self.root)

    def _tree_to_dna_rek(self, node):
        # append dna-string with node-name
        return_string = translate_to_dna(node.name, self.version)

        # check if node has subtree
        if len(node.children) == self.branching_degree:
            # append dna-string with open bracket
            return_string += translate_to_dna("(", self.version)
            # append dna-string with subtree-string
            counter = 0
            for child in node.children:
                counter += 1
                ret_string = self._tree_to_dna_rek(child)
                return_string += ret_string
                if counter < self.branching_degree:
                    return_string += translate_to_dna(",", self.version)
        return return_string

    def tree_from_dna(self, string):
        normal_string = translate_from_dna(string, self.version)
        tree_string = Tp.add_closing_brackets(normal_string, self.branching_degree)
        return super()._initialize_with_string_rek(tree_string)
