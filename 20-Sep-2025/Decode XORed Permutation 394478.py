# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n, acc2 = len(encoded), 0 
        acc1 = reduce(lambda x, y: x^y,range(1, n+2))
        for i in range(0,n,2): 
            acc2 ^= encoded[i] 
        return list(accumulate(encoded[::-1], xor, initial = acc1^acc2))[::-1]