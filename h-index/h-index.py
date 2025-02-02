class Solution:
    def hIndex(self, citations):
        citations.sort()
        n=len(citations)
        for i,v in enumerate(citations):
            if n-i <= v:
                return n-i
        return 0
        
        
        return count
