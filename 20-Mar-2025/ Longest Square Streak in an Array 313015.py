# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums) 
        max_count = -1 

        for num in nums:
            count = 0
            while num in num_set:
                count += 1
                num *= num  
            
            if count >= 2:
                max_count = max(max_count, count)

        return max_count
