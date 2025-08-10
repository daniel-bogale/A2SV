# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        
        power_set = []
        current_subset = []

        def backtracking(i):
            if i == n:
                power_set.append(current_subset[:])
                return
            
            current_subset.append(nums[i])
            backtracking(i+1) 
            current_subset.pop()
            backtracking(i+1)            

        backtracking(0)
        return power_set