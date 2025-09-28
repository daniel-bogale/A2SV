# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        self.children = [None] *26
        self.is_end = False
        

    def insert(self, word: str) -> None:
        current = self
        for char in word:
            idx = ord('a')-ord(char)
            if not current.children[idx]:
                current.children[idx] = Trie()
            current = current.children[idx]
        current.is_end = True
        
    def search(self, word: str) -> bool:
        current = self

        for char in word:
            idx = ord('a')-ord(char)
            if not current.children[idx]:
                return False

            current = current.children[idx]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self
        for char in prefix:
            idx = ord('a')-ord(char)
            if not current.children[idx]:
                return False            
            current = current.children[idx]
        return True
             

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)