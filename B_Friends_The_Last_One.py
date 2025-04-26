t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    sum = 0
    for i,num in enumerate(arr):
        sum += max(num, arr[(i+1)%len(arr)])+1
    
    print("YES" if sum<=m else "NO")