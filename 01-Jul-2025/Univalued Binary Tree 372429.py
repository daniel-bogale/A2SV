# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True 
        
        def dfs(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return dfs(node.left, value) and dfs(node.right, value)
        
        return dfs(root, root.val)
