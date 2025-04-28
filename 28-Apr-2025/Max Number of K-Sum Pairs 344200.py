# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numCounter = Counter(nums)
        count = 0
        for num in nums:
            if numCounter[num] > 0 and numCounter[k - num] > 0:
                if num == k - num and numCounter[num] < 2:
                    continue  # need two of the same number
                count += 1
                numCounter[num] -= 1
                numCounter[k - num] -= 1
        return count
