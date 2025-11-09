# Problem: Detect Cycle In An Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from collections import defaultdict, deque

class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        for start in range(V):
            if start not in visited:
                queue = deque()
                queue.append((start, -1)) 

                while queue:
                    u, parent = queue.popleft()

                    if u in visited:
                        continue
                    visited.add(u)

                    for neighbor in graph[u]:
                        if neighbor not in visited:
                            queue.append((neighbor, u))
                        elif neighbor != parent:
                            return True 

        return False