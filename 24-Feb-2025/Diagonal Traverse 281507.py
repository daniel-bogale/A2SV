# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        isUpDirection = True
        answer = []

        row_length = len(mat)
        col_length = len(mat[0])

        current_row = 0
        current_col = 0

        def next_exist(i,j,isUpDirection):
            if isUpDirection:
                i-=1
                j+=1
            else:
                i+=1
                j-=1
            return 0 <= i < row_length and 0 <= j < col_length
        
        
        while current_row < row_length and current_col < col_length:
            value = mat[current_row][current_col]
            answer.append(value)
            
            has_next = next_exist(current_row,current_col,isUpDirection)
            if isUpDirection:
                if has_next:
                    current_row-=1
                    current_col+=1
                else:
                    isUpDirection = False
                    if current_col+1 < col_length:
                        current_col+=1
                    else:
                        current_row+=1
            else:
                if has_next:
                    current_row+=1
                    current_col-=1
                else:
                    isUpDirection = True
                    if current_row+1 < row_length:
                        current_row+=1
                    else:
                        current_col+=1
        return answer
                