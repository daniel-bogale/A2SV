t = int(input())
for _ in range(t):
    length = int(input())
    S = input()
    
    r=length-1
    
    while r>=0:
        if S[r] == ")":
            r-=1
        else:
            break
    print ("Yes" if r== -1 or r < length-2-r else "No")
