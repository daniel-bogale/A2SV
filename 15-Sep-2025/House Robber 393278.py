# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def better_sum(i):
            if i >= len(nums):
                return 0
            
            two_jump = memo[i+2] if i+2 in memo else better_sum(i+2)
            three_jump = memo[i+3] if i+3 in memo else better_sum(i+3)

            memo[i+2] = two_jump
            memo[i+3] = three_jump

            return nums[i]+max(two_jump,three_jump)

        if len(nums)<=1:
            return sum(nums)
        
        return max(better_sum(0), better_sum(1))