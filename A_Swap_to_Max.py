t = int(input())
for _ in range(t):
    n= int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    for i in range(n):
        if a[i] > b[i]:
            temp= a[i]
            a[i]=b[i]
            b[i] = temp
    
    a_max=max(a)
    b_max=max(b)
    print(a_max * b_max)