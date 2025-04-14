# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

length = int(input())
arr = list(map(int, input().split()))
left = 0
right = length-1
first_sum = 0
second_sum = 0
i = 0

while left<=right:
    is_left_max = arr[left] >= arr[right]
    to_be_add = arr[left] if is_left_max else arr[right]
    
    if i%2 == 0:
        first_sum+=to_be_add
    else:
        second_sum+=to_be_add
        
    if is_left_max:
        left+=1
    else:
        right-=1
        
    i+=1
print(first_sum, second_sum)
    