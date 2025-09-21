# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            tmp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = tmp

        return a if a <= MAX_INT else ~(a ^ mask)