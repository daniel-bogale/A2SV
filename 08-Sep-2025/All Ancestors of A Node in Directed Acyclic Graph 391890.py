# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        ancestors = [set() for _ in range(n)]
        
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        while q:
            node = q.popleft()
            
            for child in graph[node]:
                ancestors[child].add(node)
                ancestors[child].update(ancestors[node])
                
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        return [sorted(list(a)) for a in ancestors]
