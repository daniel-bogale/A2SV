# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        arr = sorted((num, freq) for num, freq in counter.items())
        ans = 0
        for i in range(1, len(arr)):
            ans += i * arr[i][1]
        return ans