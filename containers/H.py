import sys
from collections import deque

data = sys.stdin.read().split()
n = int(data[0])
i = 1

left = deque()
right = deque()
out = []

for _ in range(n):
    c = data[i]
    i += 1
    if c == "+":
        right.append(int(data[i]))
        i += 1
        if len(right) > len(left):
            left.append(right.popleft())
    elif c == "*":
        left.append(int(data[i]))
        i += 1
        if len(left) > len(right) + 1:
            right.appendleft(left.pop())
    else:
        out.append(str(left.popleft()))
        if len(left) < len(right):
            left.append(right.popleft())

print("\n".join(out))
