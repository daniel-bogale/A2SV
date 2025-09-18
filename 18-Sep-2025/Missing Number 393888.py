# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)+1):
            total_sum+=i
        return total_sum-sum(nums)