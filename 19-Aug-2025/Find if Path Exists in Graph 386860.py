# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()

        def dfs(node):
            if node == destination:   
                return True
            if node in visited:      
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            return False

        return dfs(source)


