# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges) + 1)) 
        def find_root(node):
            if root[node] != node:
                root[node] = find_root(root[node])
            return root[node] 
        for node1, node2 in edges: 
            root1, root2 = find_root(node1), find_root(node2)

            if root1 == root2:
                return [node1, node2] 
 
            root[root2] = root1 