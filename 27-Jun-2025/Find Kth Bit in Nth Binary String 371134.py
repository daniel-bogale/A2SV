# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        def get_string(n):
            if n==1:
                return "0"
            prev = get_string(n-1)
            reversed_prev = reversed(prev)
            inverted_string = "".join(['1' if bit == '0' else '0' for bit in reversed_prev])

            return prev + "1" + inverted_string
        
        return get_string(n)[k-1]
        
