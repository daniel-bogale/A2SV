# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        def decodeRec(i):
            curr_str = ""
            curr_num = 0

            while i < len(s):
                if s[i].isdigit():
                    curr_num = curr_num * 10 + int(s[i])
                elif s[i] == "[":
                    inner_str, next_i = decodeRec(i + 1)
                    curr_str += curr_num * inner_str
                    curr_num = 0
                    i = next_i
                elif s[i] == "]":
                    return curr_str, i
                else:
                    curr_str += s[i]
                i += 1
            return curr_str, i

        result, _ = decodeRec(0)
        return result
