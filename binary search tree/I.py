import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check(node):
    if node is None:
        return 0
    a = check(node.left)
    b = check(node.right)
    if a == -1 or b == -1 or abs(a - b) > 1:
        return -1
    return 1 + max(a, b)


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

if check(root) == -1:
    print("NO")
else:
    print("YES")