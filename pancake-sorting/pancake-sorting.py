class Solution:
    def pancakeSort(self, arr):
        def flip(end):
            start=0
            while(start<end):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        output=[]
        for i in range(len(arr)-1,-1,-1):
            m=i
            for j in range(i,-1,-1):
                if(arr[j]>arr[m]): m=j
            if(m is not i):
                flip(m)
                flip(i)
                output.append(m+1)
                output.append(i+1)
        return output
