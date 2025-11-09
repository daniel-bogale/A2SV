# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        for arr in reversed(bucket):
            for num in arr:
                result.append(num)
                if len(result) == k:
                    return result