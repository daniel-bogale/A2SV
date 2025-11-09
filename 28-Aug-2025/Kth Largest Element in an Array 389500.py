# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        
        def heapify_down(heap, idx, size):
            while True:
                smallest = idx
                left = 2 * idx + 1
                right = 2 * idx + 2
                
                if left < size and heap[left] < heap[smallest]:
                    smallest = left
                if right < size and heap[right] < heap[smallest]:
                    smallest = right
                
                if smallest != idx:
                    heap[idx], heap[smallest] = heap[smallest], heap[idx]
                    idx = smallest
                else:
                    break
        
        heap = nums[:k]

        for i in range(k//2 - 1, -1, -1):
            heapify_down(heap, i, k)
        
        for num in nums[k:]:
            if num > heap[0]: 
                heap[0] = num
                heapify_down(heap, 0, k)
        
        return heap[0]
