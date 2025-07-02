# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_symmetry(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            return check_symmetry(left_node.left, right_node.right) and check_symmetry(left_node.right, right_node.left)
    
        if not root:
            return True
        return check_symmetry(root.left, root.right)
