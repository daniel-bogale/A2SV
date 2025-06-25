# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def countNode(node):
            if not node:
                return 0
            return 1 + countNode(node.left) + countNode(node.right)

        root_rank = countNode(root.left) + 1
        if root_rank == k:
            return root.val
        elif root_rank > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - root_rank)