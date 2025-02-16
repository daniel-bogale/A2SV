# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        val_key = {value: key for key, value in enumerate(nums)}
        answer =nums[:]
        for old_val,new_val in operations:
            idx = val_key[old_val]
            answer[idx] = new_val
            val_key.pop(old_val)
            val_key[new_val] = idx


        return answer

        