n = int(input())
volume = list(map(int,input().split()))
capability = list(map(int,input().split()))

if n <=2:
    print("YES")
else:
    total = sum(volume)
    capability.sort()
    print("YES" if capability[-1] + capability[-2] >= total else "NO")
