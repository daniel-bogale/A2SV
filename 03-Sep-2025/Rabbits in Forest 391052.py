# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        k_count = Counter(answers)
        total = 0
        for key,val in k_count.items():
            group_size = key+1

            group_count = val//group_size
            reminder = val%group_size

            total += group_count * group_size
            if reminder > 0:
                total += group_size
        
        return total
