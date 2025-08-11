# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R_len = len(board)
        C_len = len(board[0])

        path = set()

        def dfs(i,j,c):
            if c == len(word):
                return True
            
            if (i < 0 or j < 0 or 
                i == R_len or j == C_len or 
                board[i][j] != word[c] or (i,j) in path):
                return False

            path.add((i,j))
            res = (dfs(i+1, j,c+1) or
                   dfs(i-1, j,c+1) or
                   dfs(i, j+1,c+1) or
                   dfs(i, j-1,c+1))
            path.remove((i,j))
            return res

        for i in range(R_len):
            for j in range(C_len):
                if dfs(i,j,0): return True
        
        return False
            