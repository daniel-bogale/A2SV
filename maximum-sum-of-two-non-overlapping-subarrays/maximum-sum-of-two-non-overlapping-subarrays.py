class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen,secondLen):
        sub1 = 0
        sub1end = firstLen
        prefixsum1 =0
        prefixsum2 =0
        n = len(nums)
        ans =0
        while sub1end <= n:
            prefixsum1 = sum(nums[sub1:sub1end])
            sub2 = sub1end
            sub2end = sub1end+secondLen
            while sub2end <=n:
                prefixsum2 = sum(nums[sub2:sub2end])
                sub2+=1
                sub2end+=1
                ans = max(ans,prefixsum1 + prefixsum2)
            sub2=0
            sub2end = secondLen
            while sub2end <= sub1:
                prefixsum2 = sum(nums[sub2:sub2end])
                sub2+=1
                sub2end+=1
                ans = max(ans, prefixsum1+prefixsum2) 
            sub1+=1
            sub1end+=1
        return ans
