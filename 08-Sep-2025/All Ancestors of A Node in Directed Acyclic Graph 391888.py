# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming_graph = defaultdict(list)
        
        for u, v in edges:
            incoming_graph[v].append(u)
        
        memo = {}

        def get_ancestors(node: int) -> set:
            if node in memo:
                return memo[node]
            
            ancestors = set()
            for parent in incoming_graph[node]:
                ancestors.add(parent)
                ancestors |= get_ancestors(parent)
            
            memo[node] = ancestors
            return ancestors

        result = []
        for i in range(n):
            result.append(sorted(get_ancestors(i)))
        
        return result