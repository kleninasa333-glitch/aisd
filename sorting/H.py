n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])

for p in points:
    print(p[0], p[1])
