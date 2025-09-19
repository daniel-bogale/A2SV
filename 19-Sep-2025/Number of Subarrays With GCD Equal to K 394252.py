# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(n,m):
            if n == m or m == 0:
                return n
            return gcd(m,n%m)

        count = 0
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1

        return count