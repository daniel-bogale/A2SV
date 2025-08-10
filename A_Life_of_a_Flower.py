t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    prev = -1
    current_height = 1
    for i in range(n):
        if arr[i] == 1:
            if prev == 1:
                current_height +=5
            else:
                current_height+=1
            prev = 1
        else:
            if prev == 0:
                current_height = -1
                break
            else:
                prev = 0
                
    print(current_height)