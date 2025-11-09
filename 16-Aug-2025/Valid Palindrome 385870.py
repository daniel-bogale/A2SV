# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s.lower():
            if ord(char) >= 97 and ord(char) <= 122  or ord(char) >= 48 and ord(char) <= 57:
                new_str+=char
        
        return new_str == new_str[::-1]