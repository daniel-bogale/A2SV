t = int(input())
for _ in range(t):
    n = int(input())
    arr_input = list(map(int, input().split()))
    
    count = {}
    for num in arr_input:
        count[num % 3] = count.get(num % 3, 0) + 1
    
    eq_num = n // 3
    arr = [0, 0, 0]
    for key in count:
        arr[key] = count[key]
    
    max_val = max(arr)
    max_idx = arr.index(max_val)
    max_diff = max_val - eq_num
    
    next_idx = (max_idx + 1) % 3
    next_val = arr[next_idx]
    
    third_idx = (max_idx + 2) % 3
    third_val = arr[third_idx]
    
    # Handle all cases
    if next_val > eq_num:
        next_extra = next_val - eq_num
        result = next_extra + 2 * max_diff
    elif third_val > eq_num:
        third_extra = third_val - eq_num
        result = 2 * third_extra + max_diff
    else:
        for_next = eq_num - next_val
        result = for_next + 2 * (max_diff - for_next)
    
    print(result)
