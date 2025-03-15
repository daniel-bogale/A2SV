N, k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

if k == 0:
    x = arr[0] - 1
    print(x if x >= 1 else -1)
elif k == N or arr[k-1] != arr[k]:
    print(arr[k-1])
else:
    print(-1) 