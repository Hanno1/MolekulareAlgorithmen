from tree import TriTree
import treeParser as Tp
from AlphabetFunctions import translate_from_dna, translate_to_dna


class DNA_Encoder(TriTree):
    """
    trivial encoding using the logarithmic alphabet
    """
    def __init__(self, root, version, initial_value=None, dna_value=None, branching_degree=3):
        """
        :param root: root of the tree
        :param version: version of the dna encoding used - either log, bracket or bracket_improved
        :param initial_value: tree can be initialized by the user given a string like a(b,c(d,e,f),32)
        :param dna_value: tree can be initialized by the user given a dna encoding - decodes into tree structure
        :param branching_degree: branching degree of the tree - normally 3
        """
        if not version and not version in ["log", "bracket", "bracket_improved", "bracket_improved2"]:
            print("Version has to be either log, bracket, bracket_improved or bracket_improved2")
            raise ValueError
        self.branching_degree = branching_degree
        self.version = version
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
        """
        recursive function for encoding tree to dna string

        :param node: node from there to start
        :return: string
        """
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
        """
        translate dna string into tree structure. First translate the string back to normal using
        translate Function from AlphabetFunctions
        This string does not contain closing brackets, so add them using the treeParser method

        :param string: string to decode into tree structure
        :return: root node
        """
        normal_string = translate_from_dna(string, self.version)
        tree_string = Tp.add_closing_brackets(normal_string, self.branching_degree)
        return super()._initialize_with_string_rek(tree_string)
    
