class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix or not matrix[0]: return None
        row_len = len(matrix)
        col_len= len(matrix[0])
        self.dp = [[0]*(col_len+1) for _ in range(row_len+1)]
        for i in range(1,row_len+1):
            for j in range(1,col_len+1):
                self.dp[i][j]=self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]+matrix[i-1][j-1]
    def sumRegion(self, row1, col1, row2, col2):
        return (self.dp[row2+1][col2+1]-self.dp[row2+1][col1]-self.dp[row1][col2+1]+self.dp[row1][col1])
