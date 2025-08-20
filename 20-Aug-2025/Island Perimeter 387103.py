# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def isValid(i,j):
            return (i>= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))

        def sum_parameter(i,j):
            total = 0
            for di,dj in directions:
                new_i, new_j = i+di, j+dj
                if not isValid(new_i, new_j):
                    total+=1
                else:
                    if grid[new_i][new_j] ==0:
                        total+=1
            return total
            
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total +=sum_parameter(i,j)

        return total                
                    


