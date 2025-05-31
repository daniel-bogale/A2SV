t = int(input())
for _ in range(t):
    word = input()
    result = ""
    right= len(word)-1
    for i in range(len(word)-1, -1, -1):
        char = word[i]
        if char == "p":
            result+="q"
        elif char== "q":
            result+="p"
        else:
            result+="w"
    print(result)