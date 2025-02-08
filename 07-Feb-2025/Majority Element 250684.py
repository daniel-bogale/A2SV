# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        max_num = count[nums[0]]
        max_key = nums[0]
        for key,val in count.items():
            if val > max_num:
                max_num = val
                max_key = key
        return max_key
