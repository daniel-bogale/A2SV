t = int(input())
for _ in range(t):
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    used = {}
    mid_count = {}

    for i, x in enumerate(a):
        if 2 * x == T:
            mid_count[x] = mid_count.get(x, 0) + 1
            ans[i] = mid_count[x] % 2
        else:
            if x not in used:
                used[x] = 0
                used[T - x] = 1
            ans[i] = used[x]
    print(*ans)
