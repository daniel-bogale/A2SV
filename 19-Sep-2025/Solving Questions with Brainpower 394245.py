# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  
        for i in range(n-1, -1, -1):
            points, skip = questions[i]
            
            solve = points
            if i + skip + 1 < n:
                solve += dp[i + skip + 1]
            
            dp[i] = max(solve, dp[i+1])
        
        return dp[0]