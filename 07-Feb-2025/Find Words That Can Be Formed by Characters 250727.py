# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            char_store = list(chars)
            is_good=True
            for char in word:
                if char in char_store:
                    char_store.remove(char)
                else:
                    is_good = False
                    break
            if is_good:
                count+=len(word)
        return count