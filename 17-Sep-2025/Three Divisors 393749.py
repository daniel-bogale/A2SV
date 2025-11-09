# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        root = int(math.isqrt(n))  
        if root * root != n:
            return False 

        if root < 2:
            return False
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False
        return True

#MK