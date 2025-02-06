# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        no_more = False
        misplaced_idx = -1
        for i,char in enumerate(s1):
            if char != s2[i]:
                if s1.find(s2[i]) == -1 or s2.find(char) == -1:
                    return False
                elif no_more:
                    return False
                elif misplaced_idx == -1:
                    misplaced_idx = i
                elif s2[i]==s1[misplaced_idx]:
                    misplaced_idx = -1
                    no_more = True
                else:
                    return False

        return misplaced_idx == -1
            
            