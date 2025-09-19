# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        counter = {}
        result = []

        for num in nums:
            if num in counter:
                result.append(num)
            else:
                counter[num] = 1
                
        return result