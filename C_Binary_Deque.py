t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    total = sum(arr)
    
    if total < s:
        print(-1)
    elif total == s:
        print(0)
    else:
        prefix_sum = 0
        prefix_positions = {0: -1} 
        max_length = 0
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if (prefix_sum - s) in prefix_positions:
                length = i - prefix_positions[prefix_sum - s]
                max_length = max(max_length, length)
            
            if prefix_sum not in prefix_positions:
                prefix_positions[prefix_sum] = i
        
        print(n - max_length)