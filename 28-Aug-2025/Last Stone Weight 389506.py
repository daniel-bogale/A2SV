# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)   
        
        while len(stones) > 1:
            y = -heapq.heappop(stones) 
            x = -heapq.heappop(stones) 
            
            if y != x:
                heapq.heappush(stones, -(y - x))
        
        return -stones[0] if stones else 0