# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        all_string = "\n".join(source)
        result_string = ""

        i = 0
        while i < len(all_string):

            two = all_string[i:i+2]
            if two == "//":
                i += 2
                while i < len(all_string) and all_string[i] != "\n":
                    i += 1

            elif two == "/*":

                i += 2
                while all_string[i:i+2] != "*/":
                    i += 1
                i += 2

            else:
                result_string += all_string[i]
                i += 1

        
        ans = []

        for line in result_string.split("\n"):
            if line != "":
                ans.append(line)
        return ans