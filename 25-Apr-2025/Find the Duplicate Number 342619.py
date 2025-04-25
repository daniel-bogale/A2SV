# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        previousVal = 0
        for num in nums:
            if previousVal== num:
                return num
            previousVal = num        