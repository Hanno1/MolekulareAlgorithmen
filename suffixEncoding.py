from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
import Constants


def generator(symbols):
    # generator for unique words of given length
    length = 0
    while True:
        length += 1
        arr = ["".join(i) for i in product(symbols, repeat=length)]
        for i in range(len(arr)):
            yield arr[i]


class SuffixEncoding(TriTree):
    def __init__(self, root, initial_value=None, dna_value=None, bracket=None, symbols=Constants.BASE_SYMBOLS,
                 branching_degree=3):
        self.mapping = dict()
        self.symbols = symbols
        self.branching_degree = branching_degree
        if initial_value:
            super().__init__(root, initial_value, branching_degree=branching_degree)
        elif dna_value and bracket:
            self.names = []
            self.root = self.tree_from_dna(dna_value, bracket)
        elif root:
            super().__init__(root)

    def tree_to_dna(self):
        # +1 for bracket terminal
        g = generator(self.symbols[1:])
        # use first encoding as bracket encoding
        self.mapping["("] = self.symbols[0]
        
        return self._tree_to_dna_rek(self.root, g)

    def _tree_to_dna_rek(self, node, g):
        # append dna-string with node-name
        self.mapping[node.name] = next(g)
        return_string = self.mapping[node.name] + self.mapping["("]

        # check if node has subtree
        if len(node.children) == self.branching_degree:
            # append dna-string with open bracket
            return_string += self.mapping["("]
            # append dna-string with subtree-string
            for child in node.children:
                ret_string = self._tree_to_dna_rek(child, g)
                return_string += ret_string
        return return_string
    
    def tree_from_dna(self, string, bracket_code):
        if bracket_code + bracket_code in string:
            split_string = string.split(bracket_code+bracket_code, 1)
            node = Node(split_string[0], self.branching_degree)
            arr = Tp.get_substring_suffix_encoding(split_string[1], bracket_code, self.branching_degree)
            node_list = []
            for n in arr:
                node_list.append(self.tree_from_dna(n, bracket_code))
            # add subtrees to root
            node.add_children(node_list)
        else:
            if string[-1] == bracket_code:
                string = string[:-1]
            node = Node(string, self.branching_degree)
            self.names.append(node.name)
        return node
