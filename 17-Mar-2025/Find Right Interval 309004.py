# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_map = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = [-1] * n

        def binary_search(target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if start_map[mid][0] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left  

        for i, (start, end) in enumerate(intervals):
            idx = binary_search(end)
            if idx < n:
                result[i] = start_map[idx][1]

        return result
