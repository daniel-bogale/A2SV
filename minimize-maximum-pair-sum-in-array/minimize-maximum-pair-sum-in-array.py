class Solution:
    def minPairSum(self, nums):
        output=[]
        nums.sort()
        for i in range(int(len(nums)/2)):
            output+=[nums[i]+nums[len(nums)-i-1]]
        return max(output)
