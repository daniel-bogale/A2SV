N = int(input())
for _ in range(N):
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))
    k= int(input())
    
    result = "YES"
    for i,val in enumerate(arr):     
        if i == 0:
            arr[i]= min(val, k-val)
        else:
            min_val = min(val, k-val)
            max_val = max(val,k-val)
            if min_val >= arr[i-1]:
                arr[i]= min_val
            elif max_val >= arr[i-1]:
                arr[i] = max_val
            else:
                result = "NO"
        
    print(result)