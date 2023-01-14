class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                
                if(nums[j]<nums[i]):
                    count+=1
            arr.append(count)

        return arr
