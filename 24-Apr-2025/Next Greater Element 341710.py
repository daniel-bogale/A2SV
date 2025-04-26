# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_map = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater_map[num] = stack[-1] if stack else -1
            stack.append(num)

        return [next_greater_map[num] for num in nums1]
