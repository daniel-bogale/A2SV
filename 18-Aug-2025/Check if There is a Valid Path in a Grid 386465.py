# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            "left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down": (1, 0),
        }
        streets = {
            1: (dirs["left"], dirs["right"]),
            2: (dirs["up"], dirs["down"]),
            3: (dirs["left"], dirs["down"]),
            4: (dirs["down"], dirs["right"]),
            5: (dirs["left"], dirs["up"]),
            6: (dirs["up"], dirs["right"]),
        }

        rows, cols = len(grid), len(grid[0])
        destination = (rows-1, cols-1)
        visited = set((0, 0))

        def is_inbound(row, col):
            return (
                0 <= row < rows
                and 0 <= col < cols
            )
        
        def dfs(row, col):
            if (row, col) == destination:
                return True
            
            for row_change, col_change in streets[grid[row][col]]:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    is_inbound(new_row, new_col)
                    and (new_row, new_col) not in visited
                    and (-row_change, -col_change) in streets[grid[new_row][new_col]]
                ):
                    visited.add((new_row, new_col))
                    if dfs(new_row, new_col):
                        return True
            return False

        return dfs(0, 0)