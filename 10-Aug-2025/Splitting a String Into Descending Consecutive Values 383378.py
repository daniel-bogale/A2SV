# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def dfs(idx,prev):
            if idx == len(s):
                return True
            for i in range(idx,len(s)):
                val = int(s[idx:i+1])
                if prev-1 == val and dfs(i+1,val):
                    return True
            return False

        for i in range(len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1,val): return True
        
        return False

        