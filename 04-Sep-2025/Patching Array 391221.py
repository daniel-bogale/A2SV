# Problem: Patching Array - https://leetcode.com/problems/patching-array/

from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1  
        count = 0 
        i = 0     
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                count += 1
        
        return count
