n = int(input())
a = list(map(int, input().split()))
st = []
need = 1

for x in a:
    st.append(x)
    while len(st) > 0 and st[-1] == need:
        st.pop()
        need += 1

if need == n + 1:
    print("YES")
else:
    print("NO")
