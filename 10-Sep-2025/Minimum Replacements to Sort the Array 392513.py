# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = nums[-1]
        result = 0


        for i in range(n - 2, -1, -1):
            parts = math.ceil(nums[i] / max_val)
            result += parts - 1
            max_val = nums[i] // parts  

        return result
