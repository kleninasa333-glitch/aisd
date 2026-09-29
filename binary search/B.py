def pribl_search(arr,x):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            found = True
            break
    if found:
        print(x)
    elif low == 0:
        print(arr[0])
    elif low == len(arr):
        print(arr[-1])
    elif x - arr[low - 1] <= arr[low] - x:
        print(arr[low - 1])
    else:
        print(arr[low])
N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in arr2:
    pribl_search(arr,i)
