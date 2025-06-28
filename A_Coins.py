t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if not n % 2:
        print("YES")
    elif not (n-k) % 2:
        print("YES")
    else:
        print("NO")