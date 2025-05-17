import sys
import math

def is_perfect_square(x):
    root = int(math.isqrt(x))
    return root * root == x

def solve(n):
    perm = []
    used = [False] * (n + 1)
    total = 0
    for i in range(n, 0, -1):
        perm.insert(0, i)
    total = 0
    for x in perm:
        total += x
        if is_perfect_square(total):
            return -1
    return perm

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        res = solve(n)
        if res == -1:
            print(-1)
        else:
            print(' '.join(map(str, res)))
