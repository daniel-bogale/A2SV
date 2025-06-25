# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        if root.left and root.left.val >=root.val:
            return False
        elif root.right and root.right.val <= root.val:
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        