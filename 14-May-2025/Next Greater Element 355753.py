# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

# from typing import List

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         next_greater_map = {}

#         for num in reversed(nums2):
#             while stack and stack[-1] <= num:
#                 stack.pop()
#             next_greater_map[num] = stack[-1] if stack else -1
#             stack.append(num)

#         return [next_greater_map[num] for num in nums1]
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for num in nums1:
            idx = 0
            while nums2[idx] != num:
                idx+=1
            nextGreater = -1
            for i in range(idx,len(nums2)):
                if num < nums2[i]:
                    nextGreater = nums2[i]
                    break
            result.append(nextGreater)
        return result