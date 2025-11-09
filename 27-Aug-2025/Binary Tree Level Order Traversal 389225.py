# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        
        def bfs(nodes):
            if not nodes:
                return

            # values of the current level
            values = [node.val for node in nodes]
            result.append(values)

            # collect next level
            nextNodes = []
            for node in nodes:
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            
            bfs(nextNodes)
        
        bfs([root])
        return result