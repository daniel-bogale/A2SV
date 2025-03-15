# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            count_less = 0
            for j in range(len(nums)):
                if i == j: 
                    continue
                if nums[j]< nums[i]:
                    count_less+=1
            answer.append(count_less)
        return answer
