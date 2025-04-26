# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prevNums = set()
        for num in nums:
            if num in prevNums:
                return num
            prevNums.add(num)