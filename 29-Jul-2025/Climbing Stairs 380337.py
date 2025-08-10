# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    memo = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in self.memo:
            return self.memo[n]
        
        if n<3:
            return n
        
        self.memo[n]= self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.memo[n]