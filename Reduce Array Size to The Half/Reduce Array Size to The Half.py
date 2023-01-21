class Solution:
    def minSetSize(self, arr):
        count=Counter(arr)
        n=len(arr)
        a=0
        output=0
        for key,val in sorted(count.items(),key=lambda x: -x[1]):
            a+=val
            output+=1
            if(a>=(n//2)): break
        return output
