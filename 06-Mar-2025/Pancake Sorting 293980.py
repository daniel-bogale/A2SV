# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def check_arr_sort(arr_check: List[int]) -> bool:
            return arr_check == sorted(arr_check)
        
        def get_max_idx(arr_max: List[int], idx: int) -> int:
            max_idx = 0
            for i in range(idx + 1): 
                if arr_max[i] > arr_max[max_idx]:
                    max_idx = i
            return max_idx

        def flip_arr(arr_flip: List[int], idx: int):
            l, r = 0, idx
            while l < r:
                arr_flip[l], arr_flip[r] = arr_flip[r], arr_flip[l]
                l += 1
                r -= 1

        answer = []
        for i in range(len(arr)-1):
            if check_arr_sort(arr):
                break
            right_limit = len(arr) - i - 1
            max_idx = get_max_idx(arr, right_limit)
            
            if max_idx != right_limit:
                if max_idx != 0:  
                    flip_arr(arr, max_idx)
                    answer.append(max_idx + 1) 

                flip_arr(arr, right_limit)
                answer.append(right_limit + 1)  

        return answer