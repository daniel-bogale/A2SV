# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        mapped = {}
        for i,val in enumerate(s):
            if val in char_map and char_map[val]!=t[i]:
                return False

            if val not in char_map:
                if t[i] in mapped:
                    return False
                char_map[val] = t[i]
                mapped[t[i]] = True
        return True