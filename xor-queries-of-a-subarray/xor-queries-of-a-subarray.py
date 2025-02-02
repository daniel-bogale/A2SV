class Solution(object):
    def xorQueries(self, arr, queries):
        A = [0]
        for a in arr:
            A.append(A[-1] ^ a)
        A.append(0)
        result = []
        for L, R in queries:
            result.append(A[L]^A[R+1])
        return result
