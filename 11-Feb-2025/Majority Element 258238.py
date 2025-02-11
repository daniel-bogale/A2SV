# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_num = (0,0)
        for key,val in count.items():
            if val > max_num[1]:
                max_num = (key, val)
        return max_num[0]
