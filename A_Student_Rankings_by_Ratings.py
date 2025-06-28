n = int(input())
a = list(map(int, input().split()))

indexed = [(a[i], i) for i in range(n)]

indexed.sort(reverse=True)

result = [0] * n

rank = 1
for i in range(n):
    if i > 0 and indexed[i][0] != indexed[i-1][0]:
        rank = i + 1
    result[indexed[i][1]] = rank

print(' '.join(map(str, result)))