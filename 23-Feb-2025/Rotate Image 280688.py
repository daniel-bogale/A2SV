# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_matrix = copy.deepcopy(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_row = j   # transpose
                new_col = i   # transpose
                new_row = len(matrix)-new_row-1  # rotate x

                matrix[i][j] = new_matrix[new_row][new_col]