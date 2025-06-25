# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, cur_min, cur_max):
            if not node:
                return cur_max - cur_min
            
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            
            left_diff = dfs(node.left, cur_min, cur_max)
            right_diff = dfs(node.right, cur_min, cur_max)
            
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)
