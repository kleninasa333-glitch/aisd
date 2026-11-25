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


def find_max_node(node):
    while node.right is not None:
        node = node.right
    return node


root = None
for s in sys.stdin.read().split():
    x = int(s)
    if x == 0:
        break
    root = insert(root, x)

parent = None
cur = root
while cur.right is not None:
    parent = cur
    cur = cur.right

if cur.left is not None:
    print(find_max_node(cur.left).data)
else:
    print(parent.data)