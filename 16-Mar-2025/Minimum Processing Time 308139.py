# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        portion = len(tasks)//len(processorTime)
        max_time =  0
        for i,val in enumerate(processorTime):
            time_take = []
            for j in range(portion):
                time_take.append(val+ tasks[j+(portion*i)])
            max_time = max(max_time, max(time_take))
        return max_time