# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_masks = {}
        max_product = 0
        
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            word_masks[word] = mask
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if word_masks[words[i]] & word_masks[words[j]] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product
