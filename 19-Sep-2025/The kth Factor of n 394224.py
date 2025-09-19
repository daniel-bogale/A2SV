# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
            if count == k:
                return i
                
        if count < k:return -1
            
