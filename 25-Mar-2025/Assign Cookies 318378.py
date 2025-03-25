# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  
        s.sort() 
        
        i, j = 0, 0 
        content_children = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]: 
                content_children += 1
                i += 1 
            j += 1 
        
        return content_children
