t = int(input())
for _ in range(t):
    n = int(input())
    str = input()
    
        
    first_A_idx = -1
    last_B_idx = -1
    for i,char in enumerate(str):
        if char == "A":
            first_A_idx = i
            break
    for i,char in enumerate(reversed(str)):
        if char == "B":
            last_B_idx = n-i-1
            break
        
    if first_A_idx == -1 or last_B_idx == -1 or first_A_idx > last_B_idx:
        print(0)
    else:
        print(last_B_idx-first_A_idx)