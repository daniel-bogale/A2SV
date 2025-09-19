# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def is_prime(n):
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False
                d += 1
            return True
        def factors_sum(n):
            res = 0
            d = 2
            while d * d <= n:
                if n % d == 0:
                    res += d
                    n = n // d
                else:
                    d += 1
            if d > 1:
                res += n
            return res
            

        while not is_prime(n):
            _sum = factors_sum(n)
            if _sum == n:
                return n
            else:
                n = _sum
        
        return n