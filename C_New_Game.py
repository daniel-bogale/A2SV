import sys
from collections import Counter

input = sys.stdin.read
data = input().split()
i = 0

t = int(data[i])
i += 1

output = []

for _ in range(t):
    n = int(data[i])
    k = int(data[i + 1])
    i += 2
    arr = list(map(int, data[i:i + n]))
    i += n

    freq = Counter(arr)
    uniq = sorted(freq)

    left = 0
    total = 0
    max_total = 0

    for right in range(len(uniq)):
        if right > 0 and uniq[right] != uniq[right - 1] + 1:
            left = right
            total = 0
        total += freq[uniq[right]]

        while right - left + 1 > k:
            total -= freq[uniq[left]]
            left += 1

        max_total = max(max_total, total)

    output.append(str(max_total))

print("\n".join(output))