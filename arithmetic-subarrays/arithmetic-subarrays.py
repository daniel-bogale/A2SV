class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        output=[]
        for i in range(len(l)):
            check=[]
            for j in range(l[i],(r[i])+1):
                check.append(nums[j]) 
            check.sort()
            for k in range(len(check)-1):
                delta=check[1]-check[0]
                if(delta!=(check[k+1]-check[k])): 
                    boolean=False
                    break
                else: boolean=True
            output.append(boolean)
        return output
