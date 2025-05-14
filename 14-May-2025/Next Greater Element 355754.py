# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for num in nums1:
            idx = 0
            while nums2[idx] != num:
                idx+=1
            nextGreater = -1
            for i in range(idx,len(nums2)):
                if num < nums2[i]:
                    nextGreater = nums2[i]
                    break
            result.append(nextGreater)
        return result