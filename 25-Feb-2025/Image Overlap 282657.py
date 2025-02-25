# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        mat_len = len(img1)

        def get_ones_positions(mat):
            return [(i, j) for i in range(mat_len) for j in range(mat_len) if mat[i][j] == 1]

        ones1 = get_ones_positions(img1)
        ones2 = get_ones_positions(img2)
        
        if not ones1 or not ones2:
            return 0

        max_overlap = 0

        shifts = Counter()

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x1 - x2, y1 - y2)
                shifts[shift] += 1
                max_overlap = max(max_overlap, shifts[shift])

        return max_overlap
