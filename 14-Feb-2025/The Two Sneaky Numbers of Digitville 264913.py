# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        exist = {}
        result = []
        for val in nums:
            if val in exist:
                result.append(val)
            else:
                exist[val] = True
        return result