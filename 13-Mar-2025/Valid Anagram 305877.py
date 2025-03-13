# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        unique_s = list(set(s))
        unique_t = list(set(t))
        if len(unique_s) != len(unique_t):
            return False
        isAnagram = True
        for char in unique_s:
            char_count = s_count[char]
            if char not in t_count:
                isAnagram = False
                break
            if char_count != t_count[char]:
                isAnagram = False
                break
        return isAnagram