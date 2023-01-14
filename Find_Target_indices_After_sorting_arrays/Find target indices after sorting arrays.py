class Solution(object):
    def targetIndices(self, nums, target):
        lessThancount = 0
        equalsCount = 0

        for i in range(0,len(nums)):
            if(nums[i]<target):
                lessThancount+=1
            if(nums[i]==target):
                equalsCount+=1
        arr = []
        if(equalsCount!=0):
            for i in range(equalsCount):
                arr.append(lessThancount+i)
        
        return arr
