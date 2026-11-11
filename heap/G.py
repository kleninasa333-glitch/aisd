import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    sizes = [int(x) for x in input_data[1:]]

    timers = [max(1000 - s, 1) for s in sizes]

    current_pos = 0
    last_record_time = 0
    time = 0

    while True:
        time += 1

        for i in range(n):
            timers[i] -= 1

        for i in range(n):
            if timers[i] == 0:
                dist = abs(i - current_pos)
                time_passed = time - last_record_time

                if dist > time_passed:
                    print(time)
                    return

                current_pos = i
                last_record_time = time
                sizes[i] += 1
                timers[i] = max(1000 - sizes[i], 1)


if __name__ == "__main__":
    solve()
