class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        
        res =[]
        l,r =0,len(nums)-1
        while len(res)!=len(nums):
            res.append(nums[l])
            l+=1
            if l <=r:
                res.append(nums[r])
                r-=1
        return res
