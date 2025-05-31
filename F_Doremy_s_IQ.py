for _ in range(int(input())):
    n, iq = map(int, input().split())
    difficulties = list(map(int, input().split()))
    result = []
    q = 0

    for problem in reversed(difficulties):
        if problem <= q:
            result.append('1')
        elif q < iq:
            result.append('1')
            q += 1
        else:
            result.append('0')

    print(''.join(reversed(result)))
