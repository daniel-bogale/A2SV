# Problem: Detect Cycle In An Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from collections import defaultdict, deque

class Solution:
    def isCycle(V, edges):

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  
    
        visited = [False] * V
    
        def dfs(node, parent):
            visited[node] = True
            for neigh in adj[node]:
                if not visited[neigh]:
                    if dfs(neigh, node):
                        return True
                elif neigh != parent
                    return True
            return False
    

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
    
        return False