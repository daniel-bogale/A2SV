t= int(input())
for _ in range(t):
    n, c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    
    mod_arr = [(val+i+1) for i,val in enumerate(arr)]
    
    mod_arr.sort()
    current_c= c
    count = 0
    for val in mod_arr:
        if current_c<val:
            break
        else:
            count+=1
            current_c-=val
    print(count)