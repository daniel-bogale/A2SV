# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh,minutes = 0, 0     

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def isValid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS  
        
        while queue and fresh>0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if isValid(row,col) and grid[row][col] == 1:
                        grid[row][col] = 2 
                        queue.append((row, col))
                        fresh -= 1
                    
            minutes +=1

        return minutes if fresh == 0 else -1
