# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0]*n
        def dfs(u):
            if color[u]:
                return color[u]==2
            color[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            color[u] = 2
            return True
        
        return [i for i in range(n) if dfs(i)]
        