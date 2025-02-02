class Solution:
    def findTheWinner(self, n, k):
        s = sorted(x+1 for x in range(n))
        cur = len(s)-1
        while len(s)>1:
            cur = (cur+k)%len(s)
            s.remove(s[cur])
            cur-=1
            cur%=len(s)
        return s[0]
