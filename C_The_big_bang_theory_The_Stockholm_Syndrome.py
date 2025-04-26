def max_possible_mex(n, a):
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
    return mex

n = int(input())
a = list(map(int, input().split()))
print(max_possible_mex(n, a))
