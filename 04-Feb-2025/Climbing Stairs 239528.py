# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo: 
                return memo[n]
            else: 
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)