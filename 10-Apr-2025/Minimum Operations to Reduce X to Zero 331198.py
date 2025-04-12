# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

"""
target = 30
max_win = -1
start = 0
end = 2
3,2,20,1,1,3
^          ^
len(arr) - max_win
5 - 3
====================

target = sum(arr) - x
max_win = -1
if len(arr) is 1 => if the ele = x return 1 else -1
start = 0
end = 1
sum(arr[start:end+1]) < target:
    end += 1
"""
# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         target = sum(nums) - x
#         max_win = -1
#         n = len(nums)
#         if n == 1:
#             return 1 if nums[0] == x else -1
#         if target == 0:
#             return n
        
#         start = 0
#         end = 0
#         s = nums[0]
#         while end < n:
#             # s = sum(nums[start:end+1])
#             if s < target:
#                 end += 1
#                 if end != n:
#                     s += nums[end]
#             else:
#                 if s == target:
#                     max_win = max(max_win, end - start + 1)                    
#                 start += 1
#                 end = start
#                 if start != n:
#                     s = nums[start]
#         return -1 if max_win == -1 else n - max_win
#         from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1  # not possible to reach x
        
        if target == 0:
            return len(nums)  # removing nothing
        
        max_win = -1
        s = 0
        start = 0

        for end in range(len(nums)):
            s += nums[end]
            
            while s > target and start <= end:
                s -= nums[start]
                start += 1
            
            if s == target:
                max_win = max(max_win, end - start + 1)
        
        return -1 if max_win == -1 else len(nums) - max_win

