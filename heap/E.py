import heapq
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    numbers = list(map(int, input_data[1:n + 1]))

    heapq.heapify(numbers)

    total_cost = 0.0

    while len(numbers) > 1:
        val1 = heapq.heappop(numbers)
        val2 = heapq.heappop(numbers)

        current_sum = val1 + val2
        total_cost += current_sum * 0.05

        heapq.heappush(numbers, current_sum)

    print(f"{total_cost:.2f}")


if __name__ == "__main__":
    solve()
