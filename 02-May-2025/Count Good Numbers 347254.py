# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_indices = (n+1)//2
        odd_indices = (n//2)

        def recurse(x,powy):
            if powy == 0:
                return 1

            half = recurse(x,powy//2)

            if powy%2:
                return (x*half*half)%1000000007
 
            return (half*half)%1000000007

        return (recurse(5, even_indices)*recurse(4,odd_indices))%1000000007