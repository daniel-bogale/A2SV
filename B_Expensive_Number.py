t= int(input())
for _ in range(t):
    num_str = input()
    left=0 
    right= len(num_str)-1
    while num_str[right] == "0" and right>0:
        right-=1

    zero_count = 0
    
    while left < right:
        if num_str[left] == "0":
            zero_count+=1
        left+=1
    print(len(num_str)-(zero_count+1))