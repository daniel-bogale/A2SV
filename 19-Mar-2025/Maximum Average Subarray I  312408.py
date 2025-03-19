# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev_sum = 0
        for i in range(k):
            prev_sum += nums[i]
        
        max_average = prev_sum/k

        for i in range(k,len(nums)):
            prev_sum-=nums[i-k]
            prev_sum+=nums[i]
            max_average= max(prev_sum/k, max_average)
        return max_average
            