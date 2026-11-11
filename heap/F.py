import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    if n == 0:
        print(0)
        return

    cargo = []
    for i in range(n):
        t = int(input_data[1 + 2*i])
        l = int(input_data[2 + 2*i])
        cargo.append((t, l))

    cargo.sort()

    import heapq
    heap = []

    for t, l in cargo:
        if heap and heap[0] <= t:
            heapq.heappop(heap)
        heapq.heappush(heap, t + l)

    print(len(heap))

if __name__ == "__main__":
    solve()
