length = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
for num in arr:
    if num < 0:
        print(num)
        break
    root = int(num ** 0.5)
    if root * root != num:
        print(num)
        break
