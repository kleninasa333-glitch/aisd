st = []

while True:
    cmd = input().split()

    if cmd[0] == "push":
        st.append(int(cmd[1]))
        print("ok")
    elif cmd[0] == "pop":
        if len(st) == 0:
            print("error")
        else:
            print(st.pop())
    elif cmd[0] == "back":
        if len(st) == 0:
            print("error")
        else:
            print(st[-1])
    elif cmd[0] == "size":
        print(len(st))
    elif cmd[0] == "clear":
        st.clear()
        print("ok")
    elif cmd[0] == "exit":
        print("bye")
        break
