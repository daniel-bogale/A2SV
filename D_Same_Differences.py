N = int(input())
for i in range(N):
    length= int(input())
    nums = list(map(int,input().split()))
    count = 0
    for i in range(length-1):
        for j in range(i+1,length):
            if nums[j] == nums[i] <=0:
                continue
            if j - i == nums[j]-nums[i]:
                count +=1
    print(count)


    
    
    
    
    
    