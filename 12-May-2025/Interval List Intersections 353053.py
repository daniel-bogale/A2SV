# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        result = []

        while first < len(firstList) and second < len(secondList):
            start1, end1 = firstList[first]
            start2, end2 = secondList[second]
            if start1 <= end2 and start2 <= end1:
                result.append([max(start1, start2), min(end1, end2)])
            if end1 < end2:
                first += 1
            else:
                second += 1
        return result
