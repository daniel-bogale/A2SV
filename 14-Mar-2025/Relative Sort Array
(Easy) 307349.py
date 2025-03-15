# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {num:0 for num in arr2}
        remaining_arr = []
        for num in arr1:
            if num in arr2_map:
                arr2_map[num]+=1
            else:
                remaining_arr.append(num)
        result = []
        for num in arr2:
            result+=[num]*arr2_map[num]  

        remaining_arr.sort()
        result+=remaining_arr

        return result