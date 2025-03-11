# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        j = 0 # Zero value elem Index
        i = 0 # counter
        while i < len(nums):
            val = nums[i]
            if val == 0:
                i += 1
            
            else:
                nums[j] = val
                j+=1
                i+=1
        print(j,len(nums))
        while j < len(nums):
            nums[j] = 0
            j+=1
        
        return nums
