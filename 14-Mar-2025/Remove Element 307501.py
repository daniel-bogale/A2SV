# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        np = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != val:
                np = i
                break
        vp = 0
        while np>vp:
            if nums[vp] != val:
                vp+=1
            else:
                nums[np], nums[vp] = nums[vp],nums[np]
                vp+=1
                while np-1 > vp and nums[np] == val:
                    np-=1       

        while len(nums)>0 and nums[-1] == val:
            nums.pop()