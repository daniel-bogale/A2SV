t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq = [0] * (n + 1)
    for x in arr:
        freq[x] += 1
    
    score = 0
    for x in range(1, n + 1):
        y = k - x
        if y < 1 or y > n:
            continue
        if x == y:
            score += freq[x] // 2
            freq[x] = 0
        else:
            pairs = min(freq[x], freq[y])
            score += pairs
            freq[x] -= pairs
            freq[y] -= pairs
    
    print(score)
