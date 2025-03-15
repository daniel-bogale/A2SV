# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        margedArr = []

        currentInterval = intervals[0]
        
        for i in range(1, len(intervals)):
            if currentInterval[1] >= intervals[i][0]:
                currentInterval[1] = max(currentInterval[1], intervals[i][1])
            else:
                margedArr.append(currentInterval)
                currentInterval = intervals[i]
        
        margedArr.append(currentInterval)
        
        return margedArr

                