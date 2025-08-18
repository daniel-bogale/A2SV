# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def DFS(i,j):
            if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'D'
                DFS(i+1,j)
                DFS(i-1,j)
                DFS(i,j+1)
                DFS(i,j-1)   
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i in [0,len(board)-1] or j in [0,len(board[0])-1]):
                    DFS(i,j) # or BFS(i,j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'D':
                    board[i][j] = 'O'