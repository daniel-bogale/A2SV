from collections import Counter
import sys
input = sys.stdin.readline  # fast input

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = Counter(arr)
    result = 0
    
    for num in list(count.keys()):
        if count[num] == 0:
            continue
        partner = k - num
        if partner not in count:
            continue
        
        if num == partner:
            result += count[num] // 2
            count[num] = 0
        elif num < partner:
            pairs = min(count[num], count[partner])
            result += pairs
            count[num] = 0
            count[partner] = 0
    
    print(result)
