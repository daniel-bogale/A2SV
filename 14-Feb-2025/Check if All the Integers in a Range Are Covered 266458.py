# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda num: num[0])
        formattedRanges = []
        temp = ranges[0]
        for range in ranges:
            if range[0] <= temp[1]+1:
                temp[1] = max(temp[1],range[1])
            else:
                formattedRanges.append(temp)
                temp=range
        formattedRanges.append(temp)
        print(formattedRanges)
        
        for range in ranges:
            if left >= range[0] and right <= range[1]:
                return True
        
        return False