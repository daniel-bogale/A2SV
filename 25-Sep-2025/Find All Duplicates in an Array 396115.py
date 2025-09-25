# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                result.append(val)
            else:
                nums[val - 1] = -nums[val - 1]
        return result
