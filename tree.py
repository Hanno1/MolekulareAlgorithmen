from treeParser import get_subtree_strings
import CustomExceptions


class Node:
    """
    Node datastructure. used by all tree algorithms
    """
    def __init__(self, name, degree):
        """
        :param name: name of the node. will be unique
        :param degree: degree of the node - either 0 children or exactly degree many (normally 3)
        """
        if "(" in name or "," in name:
            print("Invalid name. Name has to contain only lowercase letters and/or digits")
            raise ValueError
        self.name = name
        self.degree = degree
        self.children = []

    def add_children(self, children):
        if len(children) != self.degree:
            raise CustomExceptions.WrongNumberChildren(len(children), self.name, self.degree)
        self.children = children


class TriTree:
    """
    normal tree structure used by all main algorithms
    """
    def __init__(self, root, initial_value=None, branching_degree=3):
        """
        :param root: root node of the tree
        :param initial_value: if this is not none, we will initialize the tree using a string like a(b,c,d(1,23,4))
        :param branching_degree: degree of the nodes contained in the tree
        """
        # self.names will save all names contained in the tree and raise an error then there are duplicates
        self.names = []
        self.branching_degree = branching_degree
        if initial_value:
            self.root = self._initialize_with_string_rek(initial_value)
        else:
            self.root = root
            self.names.append(self.root.name)
        
    def _initialize_with_string_rek(self, string):
        """
        initialize the graph using a string given by the user
        :return: node
        """
        # if the string contains a bracket we have to disassemble once more
        if "(" in string:
            split_string = string.split("(", 1)
            node = Node(split_string[0], self.branching_degree)
            self.names.append(node.name)
            arr = get_subtree_strings(split_string[1], self.branching_degree)
            node_list = []
            for n in arr:
                # recursive call for next levels
                node_list.append(self._initialize_with_string_rek(n))
            node.add_children(node_list)
        # else - the string is simple, only a name
        else:
            node = Node(string, self.branching_degree)
            self.names.append(node.name)
        return node

    def add_node(self, node_name, children):
        """
        add node to the graph given the name of the parent node and the names of the children

        :param node_name: name of the parent node
        :param children: names of the children nodes
        """
        node = self.search_node(node_name)

        # check if node exists and if it has no children
        if not node or node.children:
            raise CustomExceptions.InvalidNode(node)
        # check for duplicate names
        for child in children:
            if child in self.names:
                raise CustomExceptions.DuplicateName(child)
        c = []
        # add children to the node
        for child in children:
            c.append(Node(child, self.branching_degree))
            self.names.append(child)
        node.add_children(c)        

    def search_node(self, name):
        # search node recursive using inorder tree traverse
        return self.inorder_find_node(self.root, name)

    def inorder_find_node(self, node, name):
        # finding node with node.name == name
        result = None
        if node.name == name:
            return node
        if len(node.children) == self.branching_degree:
            for child in node.children:
                result = self.inorder_find_node(child, name)
                if result:
                    return result
        return result

    def get_tree_string(self):
        # gets the original bracket structure of the tree
        return self._print_tree_rek(self.root)

    def _print_tree_rek(self, node):
        """
        gets a start node and disassembles the children of the node recursively and adds all substrings
        to a string representing the graph

        :param node: node from there to start
        :return: string representation of the current node
        """
        return_string = node.name
        if len(node.children) == self.branching_degree:
            return_string += "("
            for child in node.children:
                return_string += self._print_tree_rek(child) + ","
            return_string = return_string[:-1]
            return_string += ")"
        return return_string
