# Problem: Path Sum - https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False

            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            
            return (dfs(node.left, currSum) or dfs(node.right, currSum))

        return dfs(root, 0)