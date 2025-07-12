n, k = map(int, input().split())
a = list(map(int, input().split()))

diffs = []
for i in range(1, n):
    diffs.append(a[i] - a[i - 1])

diffs.sort(reverse=True)

total_cost = a[-1] - a[0]

for i in range(k - 1):
    total_cost -= diffs[i]

print(total_cost)
