# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 0

        prev_right = float("-inf")

        for point in points:
            if point[0] > prev_right:
                count +=1
                prev_right = point[1]
            else:
                prev_right = min(prev_right, point[1])
        
        return count


