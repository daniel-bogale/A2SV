class Solution(object):
    
    def largestNumber(self, nums):
        
        for k,n in enumerate(nums):
            nums[k]=str(n)
        i=0
        while i < len(nums):
            j=i+1
            while j <len(nums):
                if nums[j]+nums[i]>nums[i]+nums[j]:
                    nums[j],nums[i]=nums[i],nums[j]
                j+=1
            i+=1
        s=""
        for num in nums:
            s+=num
        return str(int(s))
            
