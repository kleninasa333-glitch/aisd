import sys

s = sys.stdin.readline().strip()
st = []
ok = True

for c in s:
    if c == "(" or c == "[" or c == "{":
        st.append(c)
    else:
        if len(st) == 0:
            ok = False
            break
        top = st.pop()
        if c == ")" and top != "(":
            ok = False
            break
        if c == "]" and top != "[":
            ok = False
            break
        if c == "}" and top != "{":
            ok = False
            break

if ok and len(st) == 0:
    print("yes")
else:
    print("no")
