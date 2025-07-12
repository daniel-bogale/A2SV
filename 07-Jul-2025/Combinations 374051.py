# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(list(path))
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  

        backtrack(1, [])
        return res
