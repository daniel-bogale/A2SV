# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop", "asdfghjkl" ,"zxcvbnm"]
        result = []
        for i,word in enumerate(words):
            word_row = -1
            for i,row in enumerate(rows):
                first_char = word[0].lower()
                if first_char in row:
                    word_row = i
                    break
            
            row = rows[word_row]
            is_in_one_row = True
            for i,char in enumerate(word):
                if char.lower() not in row:
                    is_in_one_row = False
                    break
            if is_in_one_row: result.append(word)
        return result

            

