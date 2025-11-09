n=int(input())
denominations = [1,5,10,20,100]
count = 0
for d in denominations[::-1]:
    count += n//d
    n %= d
print(count)
