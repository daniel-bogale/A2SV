t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    occupied = set()
    follows = "YES"
    
    for i, seat in enumerate(arr):
        if i == 0:
            occupied.add(seat)
            continue

        if (seat - 1 not in occupied) and (seat + 1 not in occupied):
            follows = "NO"
            break
        occupied.add(seat)
    
    print(follows)
