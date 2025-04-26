length = int(input())
arr = list(map(int, input().split()))
left = 0
right = length - 1
first_sum = 0
second_sum = 0
i = 0

while left <= right:
    if arr[left] >= arr[right]:
        to_be_add = arr[left]
        left += 1
    else:
        to_be_add = arr[right]
        right -= 1

    if i % 2 == 0:
        first_sum += to_be_add  # Sereja's turn
    else:
        second_sum += to_be_add  # Dima's turn

    i += 1

print(first_sum, second_sum)
