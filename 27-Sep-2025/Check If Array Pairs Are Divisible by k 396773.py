# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = Counter([num % k for num in arr])
        
        for r in range(k):
            if r == 0:
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        return True