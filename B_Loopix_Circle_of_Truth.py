t = int(input())
for _ in range(t):
    s = input().strip()
    countN = s.count('N')
    if countN == 1:
        print("NO")
    else:
        print("YES")