# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = {}

        while True:
            if n in prev_nums:
                return False
            if n == 1:
                return True
            
            prev_nums[n] = True
            n = sum([int(i)**2 for i in str(n)])