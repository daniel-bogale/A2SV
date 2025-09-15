# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def jump(n):
            if n <=0:
                return 0
            if n <=2:
                return n
            N_1 = memo[n-1] if n-1 in memo else jump(n-1)
            N_2 = memo[n-2] if n-2 in memo else jump(n-2)
            memo[n] = N_1+N_2
            return N_1+N_2
        return jump(n)