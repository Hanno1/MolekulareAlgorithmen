from treeParser import get_subtree_strings
import CustomExceptions


class Node:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
        self.parent = None
        self.children = []

    def add_children(self, children):
        if len(children) != self.degree:
            raise CustomExceptions.WrongNumberChildren(len(children), self.name, self.degree)
        self.children = children
        for child in children:
            child.parent = self


class TriTree:
    def __init__(self, root, initial_value=None, branching_degree=3):
        self.names = []
        self.branching_degree = branching_degree
        if initial_value:
            self.root = None
            self.root = self._initialize_with_string_rek(initial_value)
        else:
            self.root = root
            self.names.append(self.root.name)
        
    def _initialize_with_string_rek(self, string):
        if "(" in string:
            split_string = string.split("(", 1)
            node = Node(split_string[0], self.branching_degree)
            self.names.append(node.name)

            arr = get_subtree_strings(split_string[1], self.branching_degree)
            node_list = []
            for n in arr:
                node_list.append(self._initialize_with_string_rek(n))
            node.add_children(node_list)
        else:
            node = Node(string, self.branching_degree)

            self.names.append(node.name)
        return node

    def add_node(self, node_name, children):
        node = self.search_node(node_name)

        if not node or node.children:
            raise CustomExceptions.InvalidNode(node)
        for child in children:
            if child in self.names:
                raise CustomExceptions.DuplicateName(child)
        c = []
        for child in children:
            c.append(Node(child, self.branching_degree))
            self.names.append(child)
        node.add_children(c)        

    def search_node(self, name):
        return self.inorder_find_node(self.root, name)

    def inorder(self, node):
        if len(node.children) == 0:
            print(node.name)
        else:
            for child in node.children:
                self.inorder(child)
            print(node.name)

    def inorder_find_node(self, node, name):
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
        return self._print_tree_rek(self.root)

    def _print_tree_rek(self, node):
        return_string = node.name
        if len(node.children) == self.branching_degree:
            return_string += "("
            for child in node.children:
                return_string += self._print_tree_rek(child) + ","
            return_string = return_string[:-1]
            return_string += ")"
        return return_string
