N = int(input())
for i in range(N):
    char_length = int(input())
    chars = list(input())
    reversed_chars = chars[::-1]
    left = 0
    right = char_length-1
    
    for i, enum  in enumerate(chars):
        left = i
        if enum == "B":
            break
    
    for i, enum in enumerate(reversed_chars):
        right = char_length-i
        if enum == "B":
            break
    
    print(right-left)