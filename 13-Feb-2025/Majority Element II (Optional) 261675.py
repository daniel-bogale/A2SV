# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counst = Counter(nums)
        return [key for key,value in counst.items() if value > len(nums)/3]
