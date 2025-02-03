# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        nearest_square = 0
        while (nearest_square+1)*(nearest_square+1) <= x:
            nearest_square+=1

        return nearest_square

        

