# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

INF = 10**18

n, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

max_value = sum(v for _, v in items)

dp = [INF] * (max_value + 1)
dp[0] = 0

for w, v in items:
    for val in range(max_value, v - 1, -1):
        dp[val] = min(dp[val], dp[val - v] + w)

ans = max(v for v in range(max_value + 1) if dp[v] <= W)
print(ans)