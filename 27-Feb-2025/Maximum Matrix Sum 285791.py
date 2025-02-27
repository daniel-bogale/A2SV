# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:      
        total_sum = 0
        min_num = inf
        negative_size = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                value = matrix[i][j]
                total_sum+= abs(value)
                min_num = min(min_num, abs(value))
                
                if value < 0:
                    negative_size+=1

        if negative_size%2 != 0:
            total_sum -= abs(2*min_num)

        return total_sum