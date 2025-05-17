def solve():
    n = int(input())
    if n == 1:
        print(-1)
        return

    if n == 2:
        print(-1)
        return

    if n == 3:
        print(-1)
        return

    p = list(range(1, n + 1))

    def is_perfect_square(k):
        if k < 0:
            return False
        sqrt_k = int(k**0.5)
        return sqrt_k * sqrt_k == k

    import itertools

    for perm in itertools.permutations(p):
        is_flawless = True
        current_sum = 0
        for i in range(n):
            current_sum += perm[i]
            if is_perfect_square(current_sum):
                is_flawless = False
                break
        if is_flawless:
            print(*perm)
            return

    print(-1)


t = int(input())
for _ in range(t):
    solve()