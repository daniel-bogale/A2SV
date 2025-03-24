# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        max_container=0
        while l<r:
            left_val =height[l]
            right_val = height[r]
            max_container = max(min(left_val,right_val)*(r-l), max_container)
            if left_val>right_val:
                r-=1
            elif left_val<right_val:
                l+=1
            else:
                if l+1 < len(height) and r-1 >=0 and height[l+1] < height[r-1]:
                    r-=1
                else:
                    l+= 1
        return max_container