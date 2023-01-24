class Solution:
    def removeKdigits(self, num, k):
        stalk=[]
        for i in (num):
            while stalk and k>0 and int(stalk[-1]) > int(i):
                k-=1
                stalk.pop()   
            stalk.append(i)
        stalk=stalk[:len(stalk)-k] 
        ans=''.join(stalk)
        return str(int(ans)) if stalk else '0'
                    
            
