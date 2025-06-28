t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if (len(arr)<2):
        print("0")
        continue
    arr.sort()
    
    gap_arr = []
    for i in range(1,len(arr)):
        num = 1 if arr[i]-arr[i-1] <= k else 0
        gap_arr.append(num)
    
    max_count = 0
    current_count = 0
    for i in range(len(gap_arr)):
        if gap_arr[i] == 1:
            current_count +=1
        else:
            max_count = max(max_count, current_count)
            current_count=0
    max_count = max(max_count, current_count)
    print(len(gap_arr)-max_count)
