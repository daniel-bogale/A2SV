# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        quantity = Counter(answers)
        total = 0
        for key,val in quantity.items():
            if key == 0:
                total +=val
            elif val <= key+1:
                total += key+1
            else:
                unpaired = val%(key+1)
                total += val
                if unpaired:
                    total+=key+1-unpaired
        return total