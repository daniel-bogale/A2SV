# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)],      # right, up
        }

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return False
            if i == m - 1 and j == n - 1:
                return True

            visited.add((i, j))

            for di, dj in dirs[grid[i][j]]:
                ni, nj = i + di, j + dj
                if isValid(ni, nj):
                    if (-di, -dj) in dirs[grid[ni][nj]]:
                        if dfs(ni, nj):
                            return True

            return False

        return dfs(0, 0)