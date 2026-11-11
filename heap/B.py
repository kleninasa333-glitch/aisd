heap = [0]


def sift_up(i):
    while i > 1 and heap[i] < heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i = i // 2


def sift_down(i):
    size = len(heap) - 1
    while 2 * i <= size:
        j = 2 * i
        if j + 1 <= size and heap[j + 1] < heap[j]:
            j = j + 1
        if heap[i] <= heap[j]:
            break
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def insert(k):
    heap.append(k)
    sift_up(len(heap) - 1)


def extract_min():
    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    if len(heap) > 1:
        sift_down(1)
    return result


n = int(input())
numbers = input().split()
for x in numbers:
    insert(int(x))

result = []
for _ in range(n):
    result.append(extract_min())

print(" ".join(map(str, result)))
