class Solution(object):
    def productExceptSelf(self, nums):
        res=[0]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix*=nums[i]
        return res
