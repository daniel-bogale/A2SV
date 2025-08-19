# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        P = (target + total_sum) // 2
        
        dp = [0] * (P + 1)
        dp[0] = 1 
        
        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[P]