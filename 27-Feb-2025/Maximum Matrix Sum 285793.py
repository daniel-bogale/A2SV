# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = sum(abs(num) for row in matrix for num in row)
        min_num = min(abs(num) for row in matrix for num in row)
        negative_count = sum(num < 0 for row in matrix for num in row)

        return total_sum - 2 * min_num if negative_count % 2 else total_sum
