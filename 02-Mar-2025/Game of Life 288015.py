# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
        def check_existance(x,y):
            return 0<= x <len(board) and 0<=y<len(board[0])

        for i in range(len(board)):
            for j in range(len(board[0])):
                count_one = 0
                current_val = board[i][j]
                for dir in dirs:
                    new_x, new_y = i+dir[0], j+dir[1]
                    if check_existance(new_x ,new_y) and (board[new_x][new_y] == 1 or board[new_x][new_y] == -1):
                        count_one +=1
                if current_val == 0 and count_one == 3:
                    board[i][j] = 2
                elif current_val == 1 and (count_one < 2 or count_one > 3):
                    board[i][j] = -1
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == -1:
                    board[i][j] = 0
                elif val == 2:
                    board[i][j] = 1
        



                        



        