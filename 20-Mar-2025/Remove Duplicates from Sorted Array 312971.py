# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
  def removeDuplicates(self, nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
          nums[k]=nums[i]
          k+=1
    return k 
        