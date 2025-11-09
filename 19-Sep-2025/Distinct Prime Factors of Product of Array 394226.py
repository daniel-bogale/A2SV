# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def prime_factors(num,hashmap):
            d = 2
            while d * d <= num:
                if num % d == 0:
                    hashmap.add(d)
                    num = num // d
                else:
                    d += 1
            if d > 1:
                hashmap.add(num)

        hashmap = set()
        for num in nums:
            if num < 2:continue
            prime_factors(num,hashmap)
        
        return len(hashmap)
            