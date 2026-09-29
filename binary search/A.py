def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    found = False
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            found = True
            break
    if found:
        print('YES')
    else:
        print('NO')
N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in arr2:
    binary_search(arr,i)
