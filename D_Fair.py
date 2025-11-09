from collections import deque
import sys
input = sys.stdin.readline

n, m, k, s = map(int, input().split())
goods = list(map(int, input().split()))

# Group towns by good type (1-indexed)
type_towns = [[] for _ in range(k + 1)]
for i, g in enumerate(goods):
    type_towns[g].append(i)

# Graph
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# Distance array: dist[i][t] = distance from town i to nearest town producing type t
dist = [[float('inf')] * k for _ in range(n)]

# Multi-source BFS for each type
for t in range(1, k + 1):
    q = deque()
    # Start from all towns producing this type
    for city in type_towns[t]:
        dist[city][t - 1] = 0
        q.append(city)
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v][t - 1] == float('inf'):
                dist[v][t - 1] = dist[u][t - 1] + 1
                q.append(v)

# For each town, compute sum of smallest s distances
for i in range(n):
    dists = sorted(dist[i])
    print(sum(dists[:s]), end=' ')
print()
