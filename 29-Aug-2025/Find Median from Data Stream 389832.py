# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = [] 
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
