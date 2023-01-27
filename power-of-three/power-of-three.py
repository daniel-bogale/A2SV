class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        else:
            return False
