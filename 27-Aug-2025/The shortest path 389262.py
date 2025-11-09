# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
a, b = map(int, input().split()) 

graph = defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

queue = deque([a])
visited = {a}
parent = {a: None}

while queue:
    node = queue.popleft()

    if node == b:
        break

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            parent[nei] = node
            queue.append(nei)

if b not in parent:
    print(-1) 
else:
    path = []
    cur = b
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(len(path) - 1)  
    print(*path)
