t= int(input())
for _ in range(t):
    n,k = map(int, input().split())
    first_arr = list(map(int,input().split()))
    second_arr = list(map(int,input().split()))
    
    first_arr.sort(reverse=True)
    second_arr.sort(reverse=True)
    
    sum= 0
    swap = 0
    f_idx = 0
    s_idx = 0
    
    for i in range(n):
        if swap < k and second_arr[s_idx]>first_arr[f_idx]:
            sum+=second_arr[s_idx]
            s_idx+=1 
            swap+=1 
        else:
            sum+=first_arr[f_idx]
            f_idx+=1
    print(sum)