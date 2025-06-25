# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        result = TreeNode()
        if root1 and root2:
            result.val = root1.val + root2.val
            result.left = self.mergeTrees(root1.left,root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            result = root1
        elif root2:
            result = root2
        else:
            result = None
        return result