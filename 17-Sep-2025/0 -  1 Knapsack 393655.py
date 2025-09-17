# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        memo = {}
        
        def dp(i,currentW):
            if i >= len(val) or currentW == 0:
                return 0
            
            if (i, currentW) not in memo:
                include = 0
                if wt[i]<= currentW:
                    include = val[i]+dp(i+1, currentW-wt[i])
                
                exclude = dp(i+1, currentW)
                
                memo[(i, currentW)] = max(include, exclude)
            
            return memo[(i, currentW)]
            
        return dp(0,W)
