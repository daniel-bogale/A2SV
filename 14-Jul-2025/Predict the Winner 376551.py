# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution(object):
    def predictTheWinner(self, nums):
        def maxDiff(start, end):
            if start == end:
                return nums[start]
            pick_start = nums[start] - maxDiff(start + 1, end)
            pick_end = nums[end] - maxDiff(start, end - 1)
            return max(pick_start, pick_end)
        return maxDiff(0, len(nums) - 1) >= 0