N = int(input())
for _ in range(N):
    n, m , k = map(int, input().split())
    a = input()
    b = input()
    # check if the length is 
    def count_sort(arr):
        arr_count = [0]*26
        for char in arr:
            idx = ord(char)-ord("a")
            arr_count[idx]+=1
        
        new_arr = ""
        for idx,count in enumerate(arr_count):
            if count > 0:
                value = chr(idx+ord("a"))
                new_arr+=value*count
                
        return new_arr

    a=count_sort(a)
    b=count_sort(b)
    
    a_p = 0
    b_p = 0
    
    a_count = 0
    b_count = 0
    
    solution = ""

    while a_p < n and b_p < m:
        if a[a_p] < b[b_p]:
            if a_count == k:
                solution+=b[b_p]
                b_p+=1
                a_count=0
                b_count=1
            else:
                solution+= a[a_p]
                a_p+=1
                a_count+=1
                b_count=0
        elif b[b_p] < a[a_p]:
            if b_count == k:
                solution+=a[a_p]
                a_p +=1
                b_count = 0
                a_count=1
            else: 
                solution+=b[b_p]
                b_p+=1
                b_count+=1
                a_count=0
    print(solution)