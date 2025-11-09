# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
a = []
b = []
c = []

for _ in range(N):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

dp = [[0]*3 for _ in range(N)]

# Base case
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i]

print(max(dp[N-1]))
