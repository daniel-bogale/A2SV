t= int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int,input().split()))
    
    freq_count = 0
    result = 0
    
    i = 0
    while i < len(arr):
        if not arr[i]:
            freq_count+=1
            if freq_count == k:
                result+=1
                i+=2
                freq_count = 0
            else:
                i+=1
        else:
            freq_count = 0
            i+=1
    print(result)