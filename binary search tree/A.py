import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find(node, x):
    while node is not None:
        if x == node.data:
            return True
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return False


def insert(node, x):
    if node is None:
        return Node(x)
    if x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node


def delete(node, x):
    if node is None:
        return None
    if x < node.data:
        node.left = delete(node.left, x)
    elif x > node.data:
        node.right = delete(node.right, x)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        m = node.left
        while m.right is not None:
            m = m.right
        node.data = m.data
        node.left = delete(node.left, m.data)
    return node


def print_tree(node, level):
    if node is None:
        return
    print_tree(node.left, level + 1)
    print("." * level + str(node.data))
    print_tree(node.right, level + 1)


root = None
for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue
    cmd = parts[0]
    if cmd == "ADD":
        x = int(parts[1])
        if find(root, x):
            print("ALREADY")
        else:
            root = insert(root, x)
            print("DONE")
    elif cmd == "DELETE":
        x = int(parts[1])
        if find(root, x):
            root = delete(root, x)
            print("DONE")
        else:
            print("CANNOT")
    elif cmd == "SEARCH":
        x = int(parts[1])
        if find(root, x):
            print("YES")
        else:
            print("NO")
    elif cmd == "PRINTTREE":
        print_tree(root, 0)