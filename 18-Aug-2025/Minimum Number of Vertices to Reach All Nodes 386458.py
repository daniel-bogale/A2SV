# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = collections.defaultdict(list)
        for src, dst in edges:
            incoming[dst].append(src)
        
        res = []
        for v in range(n):
            if not incoming[v]:
                res.append(v)
        
        return res