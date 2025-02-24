# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        dir = [(0,0), (0,1), (0,2),(1,1),(2,0),(2,1),(2,2)]
        max_sum = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                arr = []
                for row,col in dir:
                    arr.append(grid[row+i][col+j])
                max_sum = max(sum(arr),max_sum)
        return max_sum