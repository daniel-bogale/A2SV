# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        prev_chars = set()
        max_length = 0
        
        while right < len(s):
            if s[right] not in prev_chars:
                prev_chars.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                prev_chars.remove(s[left])
                left += 1

        return max_length
