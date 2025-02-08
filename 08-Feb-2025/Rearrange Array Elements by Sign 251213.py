# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num >= 0]
        negative = [num for num in nums if num < 0]
        N = len(nums)
        answer = [0]*N
        for i in range(N):
            if i % 2:
                answer[i] = negative[i//2]
            else:
                answer[i] = positive[i//2]
        return answer
        