# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
            else:
                prev_end = end
        
        return count