class Solution:
    def numIdenticalPairs(self, nums):
        
        count = Counter(nums)
        res =0
        
        for num,val in count.items():
            res+=val*(val-1)//2
        return res
         
