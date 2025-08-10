n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
max_elem = max(arr)

if total % 2 == 0 and max_elem <= total - max_elem:
    print("YES")
else:
    print("NO")
