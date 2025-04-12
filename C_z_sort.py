n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)
res = [0] * n
left = 0
right = n - 1

for i in range(n):
    if i % 2 == 0:
        res[i] = a_sorted[left]
        left += 1
    else:
        res[i] = a_sorted[right]
        right -= 1

possible = True
for i in range(1, n):
    if i % 2 == 1:
        if res[i] < res[i-1]:
            possible = False
            break
    else:
        if res[i] > res[i-1]:
            possible = False
            break

if possible:
    print(' '.join(map(str, res)))
else:
    print("Impossible")