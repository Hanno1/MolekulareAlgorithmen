from tree import TriTree
import math
from itertools import product


def generator(length):
    symbols = ["A", "C", "T", "G"]
    l = ["".join(i) for i in product(symbols, repeat=length)]
    for i in range(len(l)):
        yield l[i]


class TrivialEncoding(TriTree):
    def __init__(self, root, initial_value=None, dna_value=None):
        if initial_value:
            super().__init__(root, initial_value)
        elif dna_value:
            self.decode_tree(dna_value)
        elif root:
            super().__init__(root)

    def encode_tree(self):
        terminal_counter = len(self.names) + 1
        word_length = math.ceil(math.log(terminal_counter, 4))

        g = generator(word_length)
        bracket = next(g)

        return self._encode_tree_rek(self.root, g, bracket)[0]

    def _encode_tree_rek(self, node, g, bracket):
        return_string = next(g)
        if len(node.children) == 3:
            return_string += bracket
            for child in node.children:
                ret_string, g = self._encode_tree_rek(child, g, bracket)
                return_string += ret_string
        return return_string, g

    def decode_tree(self, string):
        pass


t = TrivialEncoding(None, "node1(node2,node3(node5,node6,node7),node4)")
print(t.encode_tree())
