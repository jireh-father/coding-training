class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False


def visit(node):
    print(node.value)


def dfs(root):
    if root is None:
        return
    visit(root)
    root.visited = True
    for child in root.children:
        if not child.visited:
            dfs(child)


def bfs(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        visit(node)
        node.visited = True
        for child in node.children:
            if not child.visited:
                queue.append(child)


root = Node(7)
root.children.append(Node(3))
root.children.append(Node(11))
root.children[0].children.append(Node(1))
root.children[0].children.append(Node(5))
root.children[1].children.append(Node(9))
root.children[1].children.append(Node(13))
root.children[0].children[0].children.append(Node(0))
root.children[0].children[0].children.append(Node(2))
root.children[0].children[1].children.append(Node(4))
root.children[0].children[1].children.append(Node(6))
root.children[1].children[0].children.append(Node(8))
root.children[1].children[0].children.append(Node(10))
root.children[1].children[1].children.append(Node(12))
root.children[1].children[1].children.append(Node(14))
bfs(root)
