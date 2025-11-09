# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = map(len, (matrix, matrix[0]))
        ans = [[0] * (C + 1) for _ in range(R + 1)]
        heap = []
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                ans[r + 1][c + 1] = cell ^ ans[r + 1][c] ^ ans[r][c + 1] ^ ans[r][c]
                heapq.heappush(heap, ans[r + 1][c + 1])
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0]  