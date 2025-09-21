# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(3)
    elif x & (x - 1) == 0:  # power of two
        print(x + 1)
    else:
        print(x & -x)