# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dir = defaultdict(int)
        for num in nums:
            dir[num] += 1
        for k,v in dir.items():
            if v == 1:
                return k
        return -1     