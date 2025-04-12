t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort() 
    left_sum = arr[0] + arr[1]
    left_count = 2
    left = 2  
    
    right_sum = arr[-1]
    right_count = 1
    right = n - 2 

    result = "NO"

    while left <= right:
        if right_sum > left_sum and right_count < left_count:
            result = "YES"
            break

        left_sum += arr[left]
        left_count += 1
        left += 1

        if left <= right:
            right_sum += arr[right]
            right_count += 1
            right -= 1

    if right_sum > left_sum and right_count < left_count:
        result = "YES"

    print(result)
