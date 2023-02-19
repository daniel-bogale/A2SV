class Solution(object):
    def longestOnes(self,nums,k):
        left = 0 
        
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1

            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            
        return len(nums) - left 
