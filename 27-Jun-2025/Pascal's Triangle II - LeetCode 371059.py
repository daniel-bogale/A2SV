# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def get_row(index):
            if index==0:
                return [1]
            if index == 1:
                return [1,1]
            new_row = [1]
            prev = get_row(index-1)
            for i in range(len(prev)-1):       
                new_row.append(prev[i]+prev[i+1])
            new_row.append(1)

            return new_row
            
        return get_row(rowIndex)