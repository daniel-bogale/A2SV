# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
        max_length = max(len(a), len(b))
        result = []

        for idx in range(max_length):
            value_1 = int(a[idx]) if idx < len(a) else 0
            value_2 = int(b[idx]) if idx < len(b) else 0
            total = value_1 + value_2 + carry
            result.append(str(total % 2))
            carry = total // 2
        
        if carry:
            result.append('1')
        
        return ''.join(result[::-1])
