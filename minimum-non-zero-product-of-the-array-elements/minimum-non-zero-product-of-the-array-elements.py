class Solution:
    def minNonZeroProduct(self, p):
        MOD = 10 ** 9 + 7
        def Cal_Pow(base, power):
            if power == 0:
                return 1
            res = Cal_Pow(base, power // 2)
            res = (res * res) % MOD
            if power % 2 == 1:
                res *= base
            return res
        biggest = 2 ** p - 1
        val = biggest - 1
        time = val // 2
        result = Cal_Pow(val, time)
        return (result * biggest) % MOD
