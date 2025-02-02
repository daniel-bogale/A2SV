class Solution(object):
    def kthLargestNumber(self, nums, k):
        return str(( sorted(nums, key= lambda p:int(p)) )[-k])
