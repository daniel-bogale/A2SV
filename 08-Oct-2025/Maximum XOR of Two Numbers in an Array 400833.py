# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        bit_size = max(nums).bit_length()

        # Build the trie
        for num in nums:
            node = root
            for i in range(bit_size - 1, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find maximum XOR
        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(bit_size - 1, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                if node.children[toggled_bit]:
                    curr_xor = (curr_xor << 1) | 1
                    node = node.children[toggled_bit]
                else:
                    curr_xor <<= 1
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)

        return max_xor
