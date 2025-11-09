# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

cache = {}
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        state = (n,k,row, column)
        if k == 0 and 0 <= row < n and 0 <= column < n:
            return 1.0
        
        if state in cache:
            return cache[state]
        
        next_moves = (
            (row - 2, column - 1), (row - 2, column + 1), (row - 1, column - 2), (row - 1, column + 2),
            (row + 2, column - 1), (row + 2, column + 1), (row + 1, column - 2), (row + 1, column + 2)
            )

        total_prob = 0.0
        for new_row, new_column in next_moves:

            if 0 <= new_row < n and 0 <= new_column < n:
                total_prob += (1 / 8) * self.knightProbability(n, k-1, new_row, new_column)

        cache[state] = total_prob
        return cache[state]
