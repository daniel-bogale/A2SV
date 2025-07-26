t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(input())    
    prev = 0
    result = "YES"
    for val in arr:
        if ord(val)<prev:
            result = "NO"
            break
        prev=ord(val)
    print(result)