t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    max_i = r // k
    if max_i < l:
        print(0)
    else:
        print(min(r, max_i) - l + 1)
