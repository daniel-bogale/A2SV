# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def countBattleships(self, board):
        return sum(
            board[i][j] == 'X' and 
            (i == 0 or board[i - 1][j] == '.') and 
            (j == 0 or board[i][j - 1] == '.')
            for i in range(len(board))
            for j in range(len(board[0]))
        )
    def findMaximumXOR(self, nums: List[int]) -> int:
        a = 0
        for i in range(31, -1, -1):
            a <<= 1
            s = {n >> i for n in nums}
            b = a | 1
            if any((b ^ x) in s for x in s):
                a = b
        return a