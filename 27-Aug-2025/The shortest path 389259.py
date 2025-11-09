# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
a, b = map(int, input().split())  # start and end

graph = defaultdict(list)

# Build the undirected graph
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(start, end):
    queue = deque([start])
    visited = {start}
    parent = {start: None}  # track parent to reconstruct path later

    while queue:
        node = queue.popleft()

        if node == end:  # stop early
            break

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                parent[nei] = node
                queue.append(nei)

    # reconstruct path if end was reached
    if end not in parent:
        return []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

path = bfs(a, b)

if path:
    print(len(path) - 1)  # number of edges
    print(*path)
else:
    print(-1)  # no path
