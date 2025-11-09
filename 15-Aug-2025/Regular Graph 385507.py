# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n,m = map(int, input().split())
degree = [0] * (n+1)
for _ in range(m):
    v1,v2= map(int, input().split())
    degree[v1] +=1
    degree[v2] +=1
if len(set(degree[1:]))==1:
    print("YES")
else:

    print("NO")
