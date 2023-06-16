from tree import TriTree
import math
from itertools import product
import tree_parser as Tp
from tree import Node


def generator(length):
    symbols = ["A", "C", "T", "G"]
    l = ["".join(i) for i in product(symbols, repeat=length)]
    for i in range(len(l)):
        yield l[i]


class TrivialEncoding(TriTree):
    def __init__(self, root, initial_value=None, dna_value=None, bracket=None):
        self.mapping = dict()
        if initial_value:
            super().__init__(root, initial_value)
        elif dna_value and bracket:
            self.names = []
            self.root = self.decode_tree(dna_value, bracket)
        elif root:
            super().__init__(root)

    def encode_tree(self):
        terminal_counter = len(self.names) + 1
        word_length = math.ceil(math.log(terminal_counter, 4))

        g = generator(word_length)
        self.mapping["("] = next(g)
        
        return self._encode_tree_rek(self.root, g)

    def _encode_tree_rek(self, node, g):
        self.mapping[node.name] = next(g)
        return_string = self.mapping[node.name]
        if len(node.children) == 3:
            return_string += self.mapping["("]
            for child in node.children:
                ret_string = self._encode_tree_rek(child, g)
                return_string += ret_string
        return return_string

    def decode_tree(self, string, bracket_code):
        if len(string) > len(bracket_code):
            node = Node(string[:len(bracket_code)])

            split_string = string[2*len(bracket_code):]

            s1, s2, s3 = Tp.parse_string2(split_string, bracket_code)
            
            n1 = self.decode_tree(s1, bracket_code)
            n2 = self.decode_tree(s2, bracket_code)
            n3 = self.decode_tree(s3, bracket_code)

            node.add_children([n1, n2, n3])
        else:
            node = Node(string)
            self.names.append(node.name)
        return node

