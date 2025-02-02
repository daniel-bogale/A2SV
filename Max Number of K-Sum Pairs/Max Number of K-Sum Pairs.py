class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        opration=0
        count=Counter(nums)
        for i in nums:
            p=k-i
            if(count[p] and count[i]>0):
                if(i==p and count[p]==1): continue
                count[p]-=1
                count[i]-=1
                opration+=1
            else: continue
        return opration
