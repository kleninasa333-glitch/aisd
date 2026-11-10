s = input().split()
st = []

for x in s:
    if x == "+":
        b = st.pop()
        a = st.pop()
        st.append(a + b)
    elif x == "-":
        b = st.pop()
        a = st.pop()
        st.append(a - b)
    elif x == "*":
        b = st.pop()
        a = st.pop()
        st.append(a * b)
    else:
        st.append(int(x))

print(st[0])
