# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Check boundaries and if cell is water or visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Mark cell as visited by setting to 0
            grid[r][c] = 0
            
            area = 1  # current cell
            # Explore neighbors (up, down, left, right)
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area
        
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area