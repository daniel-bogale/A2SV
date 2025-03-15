# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_two_sum = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                value = -(nums1[i]+nums2[j])
                first_two_sum[value] = first_two_sum.get(value,0)+1
        count= 0 
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                value = nums3[i] + nums4[j]
                if value in first_two_sum:
                    count+=first_two_sum[value]
        return count

        
            

        