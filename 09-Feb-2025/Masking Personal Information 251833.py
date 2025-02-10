# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            words = s.split("@")
            name = words[0].lower()
            val = name[0] + "*****" + name[-1]
            return val+"@"+words[1].lower()
        elif "." in s:
            return s.lower()
        else:
            num = s.replace("-", "").replace("(", "").replace(")", "").replace("+", "").replace(" ", "")
            N= len(num)
            country_code = N-10
            last_digits = num[-4:]
            prev_mask = ""
            if country_code==0:
                prev_mask = "***-***-"
            elif country_code==1:
                prev_mask = "+*-***-***-"
            elif country_code==2:
                prev_mask = "+**-***-***-"
            else:
                prev_mask = "+***-***-***-"
            return prev_mask + last_digits



                



