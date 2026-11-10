from collections import deque

q = deque()

while True:
    cmd = input().split()

    if cmd[0] == "push":
        q.append(int(cmd[1]))
        print("ok")
    elif cmd[0] == "pop":
        if len(q) == 0:
            print("error")
        else:
            print(q.popleft())
    elif cmd[0] == "front":
        if len(q) == 0:
            print("error")
        else:
            print(q[0])
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "clear":
        q.clear()
        print("ok")
    elif cmd[0] == "exit":
        print("bye")
        break
