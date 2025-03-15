# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort() 
        unique = list(set(nums))
        unique.sort()
        freq_dict = Counter(nums)
        steps = 0
        for i in range(len(unique)):
            num = unique[i]
            steps += freq_dict[num] * i  
        
        return steps  
