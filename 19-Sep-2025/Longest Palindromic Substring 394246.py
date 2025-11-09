# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        window =  len(s)
        while window > 1:
            tmp = ''
            for i in range(window):
                tmp = tmp + s[i]
            if tmp == tmp[::-1]:
                return tmp
            for i in range(window , len(s)):
                tmp = tmp[1:] + s[i]
                if tmp == tmp[::-1]:
                    return tmp

            window -= 1
        return s[0]        