# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        val_count = Counter(nums)
        pair_count = 0
        single_count = 0
        for _,val in val_count.items():
            pair_count+= val//2
            single_count+= val%2
        return [pair_count,single_count]