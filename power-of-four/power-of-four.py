class Solution(object):
    def isPowerOfFour(self, n):
        count=0
        if n==1:
            return True
        else:
            while n%4==0 and n//4>=1:
                n=n//4
                count+=1
        if n==1 and count>=1:
            return True
        else:
            return False
