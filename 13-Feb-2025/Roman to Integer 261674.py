# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        romanIntPair = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        subtractPair = {
            "I":["V","X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        int_num = 0

        for i,val in enumerate(s):
            if val in subtractPair and len(s)>i+1 and s[i+1] in subtractPair[val]:
                int_num -= romanIntPair[val]

            else: 
                int_num += romanIntPair[val]
        return int_num


    