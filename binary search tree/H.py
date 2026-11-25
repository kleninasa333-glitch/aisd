import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def branches(node):
    if node is None:
        return
    branches(node.left)
    if (node.left is None) != (node.right is None):
        print(node.data)
    branches(node.right)


root = None
for s in sys.stdin.read().split():
    x = int(s)
    if x == 0:
        break
    if root is None:
        root = Node(x)
        continue
    cur = root
    while True:
        if x == cur.data:
            break
        if x < cur.data:
            if cur.left is None:
                cur.left = Node(x)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(x)
                break
            cur = cur.right

branches(root)