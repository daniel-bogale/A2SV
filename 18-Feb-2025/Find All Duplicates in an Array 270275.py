# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            value = abs(nums[i])-1
            if nums[value] < 0:
                duplicates.append(value+1)
            else:
                nums[value] = -(nums[value])
        return duplicates