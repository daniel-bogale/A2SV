# n = int(input())
# arr = list(map(int,input().split()))

# # 0 -> rest
# # 1 -> contest
# # 2 -> gym
# # 3 -> either of them
# prev = 0
# rest_count = 0
# for num in arr:
#     if num == 0:
#         rest_count +=1
#         prev = num
    
#     elif num == 3:
#         if prev == 0:
#             continue
#         else:
#             if prev ==1:
#                 prev = 2
#             else:
#                 prev=1

#     elif prev == num:
#         rest_count +=1
#         prev = 0
        
#     else:
#         prev = num
        
# print(rest_count)    

n = int(input())
arr = list(map(int,input().split()))

# prev meaning:
# 0 = rest
# 1 = contest
# 2 = gym

prev = 0  
rest_count = 0

for num in arr:
    if num == 0:
        rest_count += 1
        prev = 0
    
    elif num == 1:
        if prev == 1:
            rest_count += 1
            prev = 0
        else:
            prev = 1

    elif num == 2:
        if prev == 2:
            rest_count += 1
            prev = 0
        else:
            prev = 2

    else:  
        if prev == 0:
            continue
        elif prev == 1:
            prev = 2
        elif prev == 2:
            prev = 1

print(rest_count)
