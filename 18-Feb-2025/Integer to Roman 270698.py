# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        max_sub_power = 0
        while 10**(max_sub_power+1) <= num:
            max_sub_power+=1

        answer = ""
        
        while max_sub_power >= 0:
            current_digit_value = num // (10**max_sub_power)
            if current_digit_value < 4:
                for i in range(current_digit_value):
                    answer+= int_roman[10**max_sub_power]
            elif current_digit_value == 4:
                answer += int_roman[10**(max_sub_power)]
                answer += int_roman[10**(max_sub_power)*5]

            elif current_digit_value == 5:
                answer+=int_roman[10**(max_sub_power)*5]

            elif current_digit_value < 9:
                answer+= int_roman[10**(max_sub_power)*5]
                addition = current_digit_value-5
                for i in range(addition):
                    answer+= int_roman[10**(max_sub_power)]

            elif current_digit_value==9:
                answer+= int_roman[10**(max_sub_power)]
                answer+=int_roman[10**(max_sub_power+1)]

            num -= current_digit_value * (10**max_sub_power)
            max_sub_power -= 1

        return answer