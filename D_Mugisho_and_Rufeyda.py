n, t = map(int,input().split(" "))
smallest_num = 10 ** (n-1)

while True:
    if smallest_num == 10 ** n:
        print(-1)
        break
    if smallest_num % t == 0:
        print(smallest_num)
        break
    smallest_num +=1