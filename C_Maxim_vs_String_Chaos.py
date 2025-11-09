from collections import defaultdict

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = input().strip()
    b = input().strip()

    pref_a = [[0]*26 for _ in range(n+1)]
    pref_b = [[0]*26 for _ in range(n+1)]

    for i in range(n):
        for c in range(26):
            pref_a[i+1][c] = pref_a[i][c]
            pref_b[i+1][c] = pref_b[i][c]
        pref_a[i+1][ord(a[i])-97] += 1
        pref_b[i+1][ord(b[i])-97] += 1

    for _ in range(q):
        l, r = map(int, input().split())
        matches = 0
        for c in range(26):
        
            count_a = pref_a[r][c] - pref_a[l-1][c]
            count_b = pref_b[r][c] - pref_b[l-1][c]
            matches += min(count_a, count_b)
        ans = (r - l + 1) - matches
        print(ans)
