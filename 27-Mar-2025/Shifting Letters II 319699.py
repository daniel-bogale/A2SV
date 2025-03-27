# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_arr = [ord(char) for char in s]
        diff = [0] * len(s_arr)
        for l, r, direction in shifts:
            direction = 1 if direction == 1 else -1
            diff[l] += direction
            if r + 1 < len(s_arr):
                diff[r + 1] -= direction

        shift_amount = 0

        for i in range(len(s_arr)):
            shift_amount += diff[i]
            s_arr[i] = (s_arr[i] - ord("a") + shift_amount) % 26 + ord("a")  # Wrap around alphabet
        
        return "".join(chr(ord_num) for ord_num in s_arr)
