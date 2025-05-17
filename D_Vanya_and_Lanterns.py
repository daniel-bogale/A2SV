n, l = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

max_gap = max(arr[0]-0, l-arr[-1])
prev = arr[0]

for num in arr:
    max_gap = max((num-prev)/2,max_gap)
    prev = num

print(max_gap)