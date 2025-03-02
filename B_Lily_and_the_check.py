N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    div = y // x
    remainder = y % x
    ans = remainder  

    exponent = 0
    while 10**exponent <= div:
        exponent += 1

    for i in range(exponent - 1, -1, -1):
        digit = div // (10**i)
        ans += digit
        div %= 10**i  

    print(ans)
