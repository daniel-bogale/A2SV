t= int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    
    dx = arr[0]-1
    dy = arr[1]-1
    
    steps = dx + (dx+1)*dy
    print("YES" if steps==arr[2] else "NO")