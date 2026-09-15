import sys

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    middle = n // 2
    first = arr[:middle]
    second = arr[middle:]

    first = merge_sort(first)
    second = merge_sort(second)

    return merge(first, second)


def merge(first, second):
    i, j = 0, 0
    answer = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            answer.append(first[i])
            i += 1
        else:
            answer.append(second[j])
            j += 1

    answer.extend(first[i:])
    answer.extend(second[j:])

    return answer


n = int(input())

if n > 10**5:
    sys.exit()

arr = list(map(int, input().split()))

for el in arr:
    if el < -10**9 or el > 10**9:
        sys.exit()

arr = merge_sort(arr)

print(*arr, sep=' ')
