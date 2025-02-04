# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())

no_of_solution = 0
for _ in range(n):
    # ptr=list(map(int,input().split(" ")))
    ptr = input().split(" ")
    for i in range(len(ptr)):
        ptr[i] = int(ptr[i])
    
    summation = sum(ptr)
    if(summation >= 2):
        no_of_solution+=1

print(no_of_solution)