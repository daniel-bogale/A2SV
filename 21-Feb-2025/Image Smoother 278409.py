# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_length = len(img)
        col_length = len(img[0])
        answer = [[0]*col_length for i in range(row_length)]
        dir = [(-1,-1), (1, 1), (-1, 1), (1, -1), (1,0), (-1,0), (0, 1), (0,-1)]

        def notOutOfBound (row_idx, col_idx):
            return 0 <= row_idx < row_length and 0 <= col_idx < col_length 

        for i in range(row_length):
            for j in range(col_length):
                elems = [img[i][j]]
                for row, col in dir:
                    new_row = row+i
                    new_col = col+j
                    if notOutOfBound(new_row,new_col):
                        elems.append(img[new_row][new_col])
                answer[i][j] = sum(elems)//len(elems)
        return answer
                
                    


