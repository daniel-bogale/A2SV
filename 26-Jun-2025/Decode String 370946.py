# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        curr_num = 0
        curr_str = ""
        stack = []
        for char in s:
            if char.isdigit():
                curr_num = curr_num*10+int(char)
            elif char == "[":
                stack.append((curr_str, curr_num))
                curr_num=0
                curr_str=""
            elif char == "]":
                prev_str, num =stack.pop()
                curr_str = prev_str+num*curr_str
            else:
                curr_str+=char
        return curr_str