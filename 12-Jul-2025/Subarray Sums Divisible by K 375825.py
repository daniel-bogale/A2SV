# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = defaultdict(int)
        count[0] = 1  
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod < 0:
                mod += k

            result += count[mod]
            count[mod] += 1

        return result