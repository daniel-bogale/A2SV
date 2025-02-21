# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        old_row_len = len(matrix)
        old_col_len = len(matrix[0])

        answer = [[0]*old_row_len for i in range(old_col_len)]

        for i in range(old_col_len):
            for j in range(old_row_len):
                answer[i][j] = matrix[j][i]

        return answer