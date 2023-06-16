from tree_parser import parse_string
import CustomExceptions


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_children(self, children):
        if len(children) != 3:
            raise CustomExceptions.WrongNumberChildren(len(children), self.name)
        self.children = children
        for child in children:
            child.parent = self


class TriTree:
    def __init__(self, root, initial_value=None):
        self.names = []
        if initial_value:
            self.root = None
            self.root = self._initialize_with_string_rek(initial_value)
        else:
            self.root = root
            self.names.append(self.root.name)
        
    def _initialize_with_string_rek(self, string):
        if "(" in string:
            split_string = string.split("(", 1)
            node = Node(split_string[0])
            self.names.append(node.name)

            s1, s2, s3 = parse_string(split_string[1])
            
            n1 = self._initialize_with_string_rek(s1)
            n2 = self._initialize_with_string_rek(s2)
            n3 = self._initialize_with_string_rek(s3)

            node.add_children([n1, n2, n3])
        else:
            node = Node(string)

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
            c.append(Node(child))
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
        if node.name == name:
            return node
        if len(node.children) == 3:
            for child in node.children:
                if self.inorder_find_node(child, name):
                    return child
        return None

    def print_tree(self):
        return self._print_tree_rek(self.root)

    def _print_tree_rek(self, node):
        return_string = node.name
        if len(node.children) == 3:
            return_string += "("
            for child in node.children:
                return_string += self._print_tree_rek(child) + ","
            return_string = return_string[:-1]
            return_string += ")"
        return return_string


tree = TriTree(Node("node1"))
tree.add_node("node1", ["node2", "node3", "node4"])
tree.add_node("node3", ["node5", "node6", "node7"])

print(tree.print_tree())

# , "node1(node2,node3,node4(node5,node6(node8,node9,node10),node7))"
"""tree.add_node(node1, [node2, node3, node4])
print(tree.print_tree())"""