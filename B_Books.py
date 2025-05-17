t, n = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
right = 0
max_book = 0

for left in range(t):
    while right < t and sum + arr[right] <= n:
        sum += arr[right]
        right += 1
    max_book = max(max_book, right - left)
    sum -= arr[left]

print(max_book)
