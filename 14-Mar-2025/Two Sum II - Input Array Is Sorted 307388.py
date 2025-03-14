# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r= len(numbers)-1
        while l<r:
            the_sum = numbers[l]+numbers[r]
            if the_sum < target:
                l+=1
            elif the_sum > target:
                r-=1
            else:
                return [l+1,r+1]
                break