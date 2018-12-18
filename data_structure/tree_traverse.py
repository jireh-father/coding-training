class Node:
    def __init__(self, value):
        self.children = [None, None]
        self.value = value


class Tree:
    def __init__(self):
        self.root = Node(7)
        self.root.children[0] = Node(3)
        self.root.children[1] = Node(11)
        self.root.children[0].children[0] = Node(1)
        self.root.children[0].children[1] = Node(5)
        self.root.children[1].children[0] = Node(9)
        self.root.children[1].children[1] = Node(13)
        self.root.children[0].children[0].children[0] = Node(0)
        self.root.children[0].children[0].children[1] = Node(2)
        self.root.children[0].children[1].children[0] = Node(4)
        self.root.children[0].children[1].children[1] = Node(6)
        self.root.children[1].children[0].children[0] = Node(8)
        self.root.children[1].children[0].children[1] = Node(10)
        self.root.children[1].children[1].children[0] = Node(12)
        self.root.children[1].children[1].children[1] = Node(14)

    def add(self, value):
        pass

    @staticmethod
    def visit(node):
        print(node.value)

    def in_order_traverse(self):
        self._in_order_traverse(self.root)

    def pre_order_traverse(self):
        self._pre_order_traverse(self.root)

    def post_order_traverse(self):
        self._post_order_traverse(self.root)

    def _in_order_traverse(self, node):
        if node is not None:
            self._in_order_traverse(node.children[0])
            self.visit(node)
            self._in_order_traverse(node.children[1])

    def _pre_order_traverse(self, node):
        if node is not None:
            self.visit(node)
            self._pre_order_traverse(node.children[0])
            self._pre_order_traverse(node.children[1])

    def _post_order_traverse(self, node):
        if node is not None:
            self._post_order_traverse(node.children[0])
            self._post_order_traverse(node.children[1])
            self.visit(node)


t = Tree()
print("in order")
t.in_order_traverse()
print("pre order")
t.pre_order_traverse()
print("post order")
t.post_order_traverse()
