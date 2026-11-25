import sys


class Node:
    __slots__ = ("data", "left", "right")

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, x):
    if node is None:
        return Node(x)
    cur = node
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
    return node


def next_value(node, x):
    best = -1
    while node is not None:
        if node.data >= x:
            best = node.data
            node = node.left
        else:
            node = node.right
    return best


n = int(sys.stdin.readline())
root = None
y = 0
after_query = False
for _ in range(n):
    op, s = sys.stdin.readline().split()
    i = int(s)
    if op == "+":
        if after_query:
            i = (i + y) % 10**9
        root = insert(root, i)
        after_query = False
    else:
        y = next_value(root, i)
        print(y)
        after_query = True