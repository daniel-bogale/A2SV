# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            lcm_val = 1
            for j in range(i, n):
                lcm_val = (lcm_val * nums[j]) // math.gcd(lcm_val, nums[j])
                
                if lcm_val == k:
                    count += 1
                elif lcm_val > k or k % lcm_val != 0:
                    break
        
        return count

# MR