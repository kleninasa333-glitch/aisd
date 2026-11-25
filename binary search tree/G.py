import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def forks(node):
    if node is None:
        return
    forks(node.left)
    if node.left is not None and node.right is not None:
        print(node.data)
    forks(node.right)


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

forks(root)