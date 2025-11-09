# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        score = 0

        def dfs(u : Optional[TreeNode] , val:str):
            nonlocal score 
            val += str(u.val)

            if u.left:
                dfs(u.left , val)

            if u.right:                 
                dfs(u.right , val)

            if not u.left and not u.right:
                score += int(val)


        dfs(root ,'')

        return score  
