t = int(input()) 

for _ in range(t):
    length = int(input())  
    arr = list(map(int, input().split()))  
    
    idx_hash = {num: i for i, num in enumerate(arr)}
    
    l, r = idx_hash[1], idx_hash[1]
    current_window = {1} 
    solution = []

    for i in range(1, length + 1):
        while len(current_window) < i:
            if l > 0 and arr[l - 1] <= i:  
                l -= 1
                current_window.add(arr[l])
            elif r + 1 < length and arr[r + 1] <= i:  
                r += 1
                current_window.add(arr[r])
            else:
                break  
        if len(current_window) == i:
            solution.append("1")
        else:
            solution.append("0")

    print("".join(solution))
