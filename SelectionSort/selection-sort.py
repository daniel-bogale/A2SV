class Solution: 
    def select(self, arr, i):
        selectionSort(arr,i) 
    
    def selectionSort(self, arr,n):
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        
        return arr
