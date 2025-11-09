import sys

MOD = 998244353

input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1
results = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    a = [0] * (n + 2)
    pos = [0] * (n + 2)
    for i in range(1, n + 1):
        a[i] = int(data[idx]); idx += 1
        pos[a[i]] = i
    
    b = [0] * (k + 1)
    in_b = [False] * (n + 2)
    for i in range(1, k + 1):
        b[i] = int(data[idx]); idx += 1
        in_b[b[i]] = True
    
    ans = 1
    for i in range(1, k + 1):
        val = b[i]
        p = pos[val]
        left = a[p - 1] if p > 1 else -1
        right = a[p + 1] if p < n else -1
        
        cnt = 0
        if left != -1 and not in_b[left]:
            cnt += 1
        if right != -1 and not in_b[right]:
            cnt += 1
        
        ans = (ans * cnt) % MOD
        in_b[val] = False  # mark as removed from a
    
    results.append(ans)

print("\n".join(map(str, results)))