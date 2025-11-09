n= int(input())
arr = list(map(int, input().split()))
print("EASY" if all(x == 0 for x in arr) else "HARD")