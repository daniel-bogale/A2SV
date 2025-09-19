# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = defaultdict(list)
    
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        res = list(s)
        
        def dfs(node, indices):
            visited[node] = True
            indices.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, indices)
        
        for i in range(n):
            if not visited[i]:
                indices = []
                dfs(i, indices)
                
                chars = sorted(res[j] for j in indices)
                for idx, ch in zip(sorted(indices), chars):
                    res[idx] = ch
        
        return "".join(res)