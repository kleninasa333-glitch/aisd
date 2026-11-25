import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, x):
    if node is None:
        return Node(x)
    if x < node.data:
        node.left = insert(node.left, x)
    elif x > node.data:
        node.right = insert(node.right, x)
    return node


def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)


root = None
for s in sys.stdin.read().split():
    x = int(s)
    if x == 0:
        break
    root = insert(root, x)

print(count(root))