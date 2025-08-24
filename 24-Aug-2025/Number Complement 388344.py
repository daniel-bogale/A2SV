# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bits = bin(num)
        bits = bits[-num.bit_length():]
        compl = []
        for bit in bits:
            compl.append("1" if bit == "0" else "0")
        return int("".join(compl), 2)