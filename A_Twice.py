from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    counted = Counter(arr)
    result = 0
    for val in counted.values():
        div = val//2
        result+= div
    print(result)