t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    forecast = list(map(int, input().split()))
    
    count = 0
    current_length = 0
    
    for temp in forecast:
        if temp <= q:
            current_length += 1
        else:
            if current_length >= k:
                valid = current_length - k + 1
                count += (valid * (valid + 1)) // 2
            current_length = 0
    
    if current_length >= k:
        valid = current_length - k + 1
        count += (valid * (valid + 1)) // 2
    
    print(count)
