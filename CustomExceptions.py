class WrongNumberChildren(Exception):
    def __init__(self, number, node_name):
        super().__init__(f"cant add {number} of children to node with name {node_name}. "
                         f"There have to be exactly 3 children")


class DuplicateName(Exception):
    def __init__(self, node_name):
        super().__init__(f"Names may not repeat themselves. Duplicated name {node_name}.")


class InvalidNode(Exception):
    def __init__(self, node_name):
        super().__init__(f"Got Invalid node {node_name}.")
