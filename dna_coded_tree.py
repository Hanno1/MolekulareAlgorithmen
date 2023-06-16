from tree import TrinärerBaum
import math
from itertools import product

symbols = ["A", "C", "T", "G"]
# def generate_rec(length):
#     c = []
#     if length == 1:
#         for i in range(4):
#             c.append(symbols[i])
#     else:
#         rec_call = generate_rec(length - 1)
#         for el in rec_call:
#             for i in range(4):
#                 c.append(el + symbols[i])
#     return c

def generator(length):
    l = ["".join(i) for i in product(symbols, repeat=length)]
    for i in range(len(l)):
        yield l[i]


class loesung1(TrinärerBaum):
    def __init__(self, root, initial_value=None, dna_value=None):
        if initial_value:
            super().__init__(root, initial_value)
        else:
            pass

    def encode_tree(self):
        terminal_counter = len(self.names) + 1
        word_length = math.ceil(math.log(terminal_counter, 4))

        g = generator(word_length)
        self.bracket = next(g)

        return self._encode_tree_rek(self.root, g)

    def _encode_tree_rek(self, node, g):
        return_string = next(g)
        if len(node.children) == 3:
            return_string += self.bracket
            for child in node.children:
                ret_string, g = self._encode_tree_rek(child, g)
                return_string += ret_string
        return return_string, g


    def decode_tree(self, string):
        pass


t = loesung1(None, "node1(node2,node3(node5,node6,node7),node4)")
print(t.encode_tree())
