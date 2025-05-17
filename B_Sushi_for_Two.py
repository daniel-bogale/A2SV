n = int(input())
arr = list(map(int, input().split()))

prev_count = 0
current_type = arr[0]
current_type_count = 0
max_count = 0

for type in arr:
    if type == current_type:
        current_type_count += 1
    else:
        max_count = max(max_count, 2 * min(prev_count, current_type_count))
        prev_count = current_type_count
        current_type = type
        current_type_count = 1

max_count = max(max_count, 2 * min(prev_count, current_type_count))

print(max_count)
