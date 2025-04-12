# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        for i in range(1, m):
            matrix[0][i] += matrix[0][i - 1]
        
        for i in range(1, n):
            cur = 0
            for j in range(m):
                cur += matrix[i][j]
                matrix[i][j] = cur + matrix[i - 1][j]
        
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cur = self.matrix[row2][col2]
        if row1 > 0:
            cur -= self.matrix[row1 - 1][col2]
        if col1 > 0:
            cur -= self.matrix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            cur += self.matrix[row1 - 1][col1 - 1]
        return cur
