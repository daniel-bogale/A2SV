n = int(input())
arr = list(map(int, input().split()))
negative_count = 0
zero_count = 0
steps = 0

for num in arr:
    if num < 0:
        negative_count += 1
        steps += -1 - num 
    elif num > 0:
        steps += num - 1  
    else: 
        zero_count += 1
        steps += 1  

if negative_count % 2 == 1 and zero_count == 0:
    steps += 2

print(steps)
