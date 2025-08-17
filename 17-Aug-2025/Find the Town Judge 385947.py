# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for x, y in trust:
            matrix[x - 1][y - 1] = 1
        
        zero_row_index = -1
        for i in range(n):
            if all(element == 0 for element in matrix[i]):
                if zero_row_index != -1:
                    return -1
                zero_row_index = i
        
        if zero_row_index == -1:
            return -1
        
        trust_count = 0
        for i in range(n):
            if matrix[i][zero_row_index] == 1:
                trust_count += 1
        if trust_count != n - 1:
            return -1
        
        return zero_row_index + 1