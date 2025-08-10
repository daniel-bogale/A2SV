t= int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    
    prev = arr[0]
    isPerfect = True
    
    for i in range(1,n):
        diff = abs(arr[i]-prev)
        if diff != 5 and diff != 7:
            isPerfect = False
            break
        prev = arr[i]
    print("YES" if isPerfect else "NO")