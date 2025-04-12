# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1  
        j = n + zeros - 1 
        
        while i >= 0:
            if j < n:
                arr[j] = arr[i]  
            j -= 1
            if arr[i] == 0:  
                if j < n:
                    arr[j] = 0
                j -= 1 
            i -= 1