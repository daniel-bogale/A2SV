# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]
        [
            dp.append(sum(dp[i - x] for x in nums if i - x >= 0))
            for i in range(1, target + 1)
        ]
        return dp[-1]