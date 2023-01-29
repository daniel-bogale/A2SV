class Solution(object):
    def moveZeroes(self, nums):
        
        i=0
        j=0
        while i<len(nums):
            current=nums[i]
            if current==0:
                i+=1
                continue
            else:
                nums[j]=current
                i+=1
                j+=1
        while j<len(nums):
            nums[j]=0
            j+=1
