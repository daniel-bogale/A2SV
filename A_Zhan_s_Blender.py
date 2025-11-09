import math
t = int(input())
for _ in range(t):
    n = int(input())
    x,y = map(int,input().split())
    
    print(math.ceil(n/min(x,y)))