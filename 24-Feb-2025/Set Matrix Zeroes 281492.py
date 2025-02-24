# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = {}
        zero_cols = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows[i] = True
                    zero_cols[j] = True
        
        for i in range(len(matrix)):
            if i in zero_rows:
                matrix[i] = [0]*len(matrix[0])
                continue
            for j in range(len(matrix[0])):
                if j in zero_cols:
                    matrix[i][j] = 0        