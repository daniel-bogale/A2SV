# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        reversePair = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack)==0 or stack[-1]!=reversePair[char]:
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0