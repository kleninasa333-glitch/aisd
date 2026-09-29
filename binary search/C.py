C = float(input())

low = 0.0
high = 100000.0

for _ in range(50):
    mid = (low + high) / 2
    if mid * mid + mid ** 0.5 < C:
        low = mid
    else:
        high = mid

print(f"{low:.9f}")
