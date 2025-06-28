n, x = map(int, input().split())
arr = list(map(int, input().split()))

current_pos = 1
possible = False
while current_pos <= x:
    if current_pos == x:
        possible = True
        break
    current_pos += arr[current_pos - 1]

print("YES" if possible else "NO")