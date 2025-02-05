N=int(input())
array = list(map(int,input().split()))
result = [""]*N
for i,val in enumerate(array):
    result[val-1] = str(i+1)
print(" ".join(result))