t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    
    modulo_arr = [num%k for num in arr]
    modulo_arr.sort()
    print(modulo_arr)    
    