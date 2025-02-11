# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i,num in enumerate(nums):
            key = target-num
            diff_dict[key] = i
       
        for i,num in enumerate(nums):
            if num in diff_dict and diff_dict[num] != i:
                return [i,diff_dict[num]]
        