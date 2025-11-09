# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def isPossible(self, row, col, cells, day):
        grid = [[0] * col for _ in range(row)]
        queue = collections.deque()
        
        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1
            
        for i in range(col):
            if not grid[0][i]:
                queue.append((0, i))
                grid[0][i] = -1

        while queue:
            r, c = queue.popleft()
            if r == row - 1:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    queue.append((nr, nc))
                    
        return False
    
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        
        while left < right:
            mid = right - (right - left) // 2
            if self.isPossible(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
                
        return left