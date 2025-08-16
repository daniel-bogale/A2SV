# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

memo = {}

def solve(i):
    if i == N - 1:
        return 0
    
    if i in memo:
        return memo[i]

    cost1 = float('inf')
    if i + 1 < N:
        cost1 = abs(stones[i] - stones[i + 1]) + solve(i + 1)
    
    cost2 = float('inf')
    if i + 2 < N:
        cost2 = abs(stones[i] - stones[i + 2]) + solve(i + 2)
    

    memo[i] = min(cost1, cost2)
    return memo[i]

N = int(input())
stones = list(map(int, input().split()))
print(solve(0))