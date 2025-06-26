# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        def helper(i):
            res = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                elif s[i] == '[':
                    decoded_str, i = helper(i + 1)
                    res += num * decoded_str
                    num = 0
                elif s[i] == ']':
                    return res, i + 1
                else:
                    res += s[i]
                    i += 1
            
            return res, i

        result, _ = helper(0)
        return result
