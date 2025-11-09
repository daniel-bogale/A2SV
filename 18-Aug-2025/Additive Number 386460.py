# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                num1 = num[:i]
                num2 = num[i:j]
                
                if (len(num1) > 1 and num1[0] == "0") or (len(num2) > 1 and num2[0] == "0"):
                    continue
                
                if self.isValid(num1, num2, num[j:]):
                    return True
        return False
    
    def isValid(self, num1: str, num2: str, remaining: str) -> bool:
        while remaining:
            sum_str = str(int(num1) + int(num2))
            if not remaining.startswith(sum_str):
                return False
            # Move forward
            num1, num2 = num2, sum_str
            remaining = remaining[len(sum_str):]
        return True
