n = int(input())

no_of_solution = 0
for _ in range(n):
    ptr = input().split(" ")
    for i in range(len(ptr)):
        ptr[i] = int(ptr[i])
    
    summation = sum(ptr)
    if(summation >= 2):
        no_of_solution+=1

print(no_of_solution)