# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            bouquets, adj = 0, 0
            for i in bloomDay:
                if i<=day:
                    adj+=1
                else:
                    adj=0
                if adj==k:
                    bouquets+=1
                    adj=0
            return bouquets                    
                    
        i, j = 0, max(bloomDay)
        res=-1
        while i<=j:
            mid=(i+j)//2
            if check(mid)>=m:
                res=mid
                j=mid-1
            else:
                i=mid+1
        return res