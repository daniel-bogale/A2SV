t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()

    prefix = [0] * n
    suffix = [0] * n

    prefix[0] = a[0] % m
    for i in range(1, n):
        prefix[i] = (prefix[i - 1] * a[i]) % m

    suffix[-1] = a[-1] % m
    for i in range(n - 2, -1, -1):
        suffix[i] = (suffix[i + 1] * a[i]) % m

    left = 0
    right = n - 1
    res = []
    for cmd in s:
        if cmd == 'L':
            res.append(suffix[left] % m)
            left += 1
        else:  # cmd == 'R'
            res.append(prefix[right] % m)
            right -= 1

    print(' '.join(map(str, res)))
