from tree import TriTree
import math
from itertools import product
import treeParser as Tp
from tree import Node
import Constants


def generator(length, symbols):
    # generator for unique words of given length
    arr = ["".join(i) for i in product(symbols, repeat=length)]
    for i in range(len(arr)):
        yield arr[i]


class LogarithmicEncoding(TriTree):
    def __init__(self, root, initial_value=None, dna_value=None, bracket=None, symbols=Constants.BASE_SYMBOLS):
        self.mapping = dict()
        self.symbols = symbols
        if initial_value:
            super().__init__(root, initial_value)
        elif dna_value and bracket:
            self.names = []
            self.root = self.decode_tree(dna_value, bracket)
        elif root:
            super().__init__(root)

    def encode_tree(self):
        # +1 for bracket terminal
        terminal_counter = len(self.names) + 1
        word_length = math.ceil(math.log(terminal_counter, len(self.symbols)))

        g = generator(word_length, self.symbols)
        # use first encoding as bracket encoding
        self.mapping["("] = next(g)
        
        return self._encode_tree_rek(self.root, g)

    def _encode_tree_rek(self, node, g):
        # append dna-string with node-name
        self.mapping[node.name] = next(g)
        return_string = self.mapping[node.name]

        # check if node has subtree
        if len(node.children) == 3: 
            # append dna-string with open bracket
            return_string += self.mapping["("]
            # append dna-string with subtree-string
            for child in node.children:
                ret_string = self._encode_tree_rek(child, g)
                return_string += ret_string
        return return_string

    def decode_tree(self, string, bracket_code):
        if len(string) > len(bracket_code):
            # get root
            node = Node(string[:len(bracket_code)])
            # get subtrees of root
            split_string = string[2*len(bracket_code):]
            s1, s2, s3 = Tp.get_substring_logarithmic_encoding(split_string, bracket_code)
            n1 = self.decode_tree(s1, bracket_code)
            n2 = self.decode_tree(s2, bracket_code)
            n3 = self.decode_tree(s3, bracket_code)
            # add subtrees to root
            node.add_children([n1, n2, n3])
        else:
            node = Node(string)
            self.names.append(node.name)
        return node
