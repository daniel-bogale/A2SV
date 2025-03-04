# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        offset = min(nums)
        length = max(nums)-offset+1
        counting=[0]*length
        for num in nums:
            counting[num-offset] += 1
        
        sorted_nums = []
        for idx,value in enumerate(counting):
            sorted_nums+=[idx+offset]*value

        answer =[]
        for idx,num in enumerate(sorted_nums):
            if num == target:
                answer.append(idx)
        return answer


