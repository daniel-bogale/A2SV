# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        
        distinct_max = set()
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            
            distinct_max.add(nums[-(i + 1)])
            if len(distinct_max) == 3:
                return nums[-(i + 1)]