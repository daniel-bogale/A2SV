# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)   
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result