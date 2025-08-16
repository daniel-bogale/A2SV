# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [-1] * N

def solve(i):
    if i == 0:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    min_cost = float('inf')
    for j in range(1, K+1):
        if i - j >= 0:
            cost = solve(i - j) + abs(h[i] - h[i - j])
            min_cost = min(min_cost, cost)
    
    dp[i] = min_cost
    return dp[i]

print(solve(N - 1))