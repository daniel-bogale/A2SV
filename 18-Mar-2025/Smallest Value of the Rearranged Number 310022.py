# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative = num < 0
        num_str = list(map(int,(list(str(abs(num))))))
        num_str.sort(reverse=isNegative)
        if num_str[0] == 0:
            for i in range(len(num_str)):
                if num_str[i] != 0:
                    num_str[i], num_str[0] = num_str[0], num_str[i]
                    break
        result = int("".join(map(str,num_str)))
        if isNegative:
            result = -result
        return result


        
