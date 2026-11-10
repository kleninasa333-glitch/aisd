from collections import deque

d = deque()

while True:
    cmd = input().split()

    if cmd[0] == "push_front":
        d.appendleft(int(cmd[1]))
        print("ok")
    elif cmd[0] == "push_back":
        d.append(int(cmd[1]))
        print("ok")
    elif cmd[0] == "pop_front":
        if len(d) == 0:
            print("error")
        else:
            print(d.popleft())
    elif cmd[0] == "pop_back":
        if len(d) == 0:
            print("error")
        else:
            print(d.pop())
    elif cmd[0] == "front":
        if len(d) == 0:
            print("error")
        else:
            print(d[0])
    elif cmd[0] == "back":
        if len(d) == 0:
            print("error")
        else:
            print(d[-1])
    elif cmd[0] == "size":
        print(len(d))
    elif cmd[0] == "clear":
        d.clear()
        print("ok")
    elif cmd[0] == "exit":
        print("bye")
        break
