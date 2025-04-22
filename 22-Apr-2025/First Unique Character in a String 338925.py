# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count=Counter(list(s))
        for i,char in enumerate(s):
            if s_count[char] == 1:
                return i
        
        return -1