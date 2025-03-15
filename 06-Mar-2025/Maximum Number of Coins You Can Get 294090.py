# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        answer = 0
        for i in range(len(piles)//3):
            answer+= piles[1+2*i]
        return answer