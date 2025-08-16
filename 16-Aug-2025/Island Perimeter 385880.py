# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        dirs = {
            "up": (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }
        print(dirs.values())
        def is_land(r, c):
            return (
                0 <= r < rows
                and 0 <= c < cols
                and grid[r][c] == 1
            )
        
        def dfs(row, col):
            if not is_land(row, col):
                return 1
            if (row, col)  in visited:
                return 0
            
            visited.add((row, col))

            perim = 0
            for row_change, col_change in dirs.values():
                new_row = row + row_change
                new_col = col + col_change
                perim += dfs(new_row, new_col)
            return perim
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]: return dfs(row, col)