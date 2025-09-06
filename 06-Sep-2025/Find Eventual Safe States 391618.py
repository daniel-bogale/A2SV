# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n 

        def dfs(node: int) -> bool:
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        result = [i for i in range(n) if dfs(i)]
        return result
