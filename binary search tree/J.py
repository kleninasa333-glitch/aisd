import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.count = 1
        self.left = None
        self.right = None


def order_up(node):
    if node is None:
        return
    order_up(node.left)
    print(node.data, node.count)
    order_up(node.right)


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
            cur.count += 1
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

order_up(root)