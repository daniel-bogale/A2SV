# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            total = 0
            if grandparent is not None and grandparent % 2 == 0:
                total += node.val
            
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total
        
        return dfs(root, None, None)
