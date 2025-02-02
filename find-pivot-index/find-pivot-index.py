class Solution(object):
    def pivotIndex(self, nums):
        summ=sum(nums)
        left_sum=0
        for i,num in enumerate(nums):
            if left_sum==summ-left_sum-num:
                return i 
            left_sum+=num
        return -1
