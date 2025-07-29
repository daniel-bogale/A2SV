# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    memo = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return n
        else:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
            return self.memo[n]