class Solution:
    def maxCoins(self ,piles):
        piles.sort()
        l = len(piles)
        i = 0
        j = 2
        k = l//3
        res = 0
        while i < k:
            res += piles[l-j]
            i+=1
            j+=2
        return res
