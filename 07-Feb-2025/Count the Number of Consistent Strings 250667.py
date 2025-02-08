# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            is_consistent = True
            for char in word:
                if not char in allowed:
                    is_consistent = False
            if is_consistent:
                count+=1

        return count