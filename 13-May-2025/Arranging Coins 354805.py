# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1, n

        while l <= r:
            mid = (l+r)//2
            sum_ = mid*(mid+1)//2

            if sum_ == n:
                return mid

            if sum_ > n:
                r = mid - 1
            else:
                l = mid + 1

        return l-1