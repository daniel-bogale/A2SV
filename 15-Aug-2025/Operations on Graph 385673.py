# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

def is_regular(graph: dict) -> bool:
    degrees = [len(neighbors) for neighbors in graph.values()]
    return all(degree == degrees[0] for degree in degrees)


n, m = map(int, input().split())
graph = dict()
for v in range(n):
    graph[v+1] = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

if is_regular(graph):
    print("YES")
else:
    print("NO")
