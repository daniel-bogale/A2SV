# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i,num in enumerate(nums):
            if i ==0:
                result.append(num)
            else:
                result.append(result[i-1]+num)
        return result