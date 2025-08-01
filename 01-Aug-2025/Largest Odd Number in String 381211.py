# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Start from the end of the string and move backwards
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:  # Check if the digit is odd
                return num[:i + 1]   # Return the substring up to that odd digit
        return ""  # No odd digit found
