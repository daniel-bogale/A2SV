# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        largest = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
            largest = max(largest, memo[i])

        return largest
