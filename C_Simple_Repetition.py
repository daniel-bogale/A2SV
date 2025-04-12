import math
def is_prime(num):
    flag = True
    if num < 2:
        flag = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
    return flag

t = int(input())
for _ in range(t):
    num, k = input().split()
    num = int(num)
    k = int(k)   
    if k > 1:
        if(num == 1 and k == 2):
            print("YES")
        else:
            print('NO')
    else:
        if is_prime(num):
            print('YES')
        else:
            print('NO')