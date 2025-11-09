# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            reduced = largest - largest // 2
            heapq.heappush(heap, -reduced)

        return -sum(heap)
