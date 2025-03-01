# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maximum=[0,0]
        for i,row in enumerate(mat):
            row_sum = sum(row)
            if row_sum > maximum[1]:
                maximum = [i,row_sum]
        return maximum