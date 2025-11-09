# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)  

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)  

            for neighbor, weight in graph[start].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, end, visited)
                if res != -1.0:
                    return res * weight

            return -1.0

        res = []
        for start, end in queries:
            res.append(dfs(start, end, set()))  

        return res
