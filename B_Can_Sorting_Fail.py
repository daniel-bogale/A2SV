t = int(input())
for _ in range(t):
    length = int(input())
    arr = list(map(int, input().split()))
    solution = "NO"
    
    for i in range(1,len(arr)):
        if max(arr[:i]) > min(arr[i:]):
            solution = "YES"
            break
    
    print(solution)