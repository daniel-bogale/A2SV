# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        carry = False  
        max_length = max(len(a), len(b))
        idx = 0
        result = ""

        while carry or idx < max_length:
            value_1 = len(a) > idx and a[idx] == "1"
            value_2 = len(b) > idx and b[idx] == "1"
            
            if value_1 and value_2 and carry:
                result += "1" 
                carry = True
            elif value_1 and value_2 and not carry:
                result += "0"  
                carry = True
            elif (value_1 or value_2) and carry:
                result += "0"  
                carry = True
            elif (value_1 or value_2) and not carry:
                result += "1"  
                carry = False
            elif not value_1 and not value_2 and carry:
                result += "1" 
                carry = False
            else:
                result += "0"  

            idx += 1  

        return result[::-1]  