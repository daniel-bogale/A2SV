# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def get_row(prev):
            row = [1]
            for i in range(len(prev)-1):
                row.append(prev[i]+prev[i+1])
            row.append(1)
            return row
        if rowIndex==0:
            return [1]
        i = 0
        output= []
        while i < rowIndex:
            output=get_row(output)
            i+=1
        return output

