# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())

s = 0
for _ in range(n):
    row = list(map(int, input().split()))
    sum_ += sum(row)

print(s // 2)