# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)

        for i in range(a, -1, -1):
            if (a / i == a // i) and ( b/ i == b // i):
                return i
        
        return 1

#GB