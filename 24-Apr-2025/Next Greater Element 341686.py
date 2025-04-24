# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def findGreaterVal(val, arr):
            res = -1
            for num in arr:
                if num > val:
                    res=num
                    break
            return res
        result = []
        for i,num1 in enumerate(nums1):
            for j,num2 in enumerate(nums2):
                if num1 == num2:
                    nextGreater = findGreaterVal(num1, nums2[j::])
                    result.append(nextGreater)
        return result