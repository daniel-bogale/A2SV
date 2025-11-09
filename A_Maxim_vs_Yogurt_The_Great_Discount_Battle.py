t = int(input())
for _ in range(t):
    n, a, b = map(int,input().split())
    
    if b < 2*a:
        print(n//2 * b + n%2*a)
    else:
        print(a*n)