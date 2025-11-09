# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(i, prevNum):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                num = int(s[i:j+1])

                if num+1 == prevNum and backtrack(j+1, num):
                    return True

            return False
        
        for i in range(len(s)-1):
            num = int(s[:i+1])
            if backtrack(i+1, num):
                return True

        return False
        
