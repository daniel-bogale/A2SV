# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                count += x % 2
                x //= 2
            ans.append(count)
        return ans
