# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:
                return False
        return not stack
