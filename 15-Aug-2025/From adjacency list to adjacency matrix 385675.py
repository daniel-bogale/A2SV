# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    for v in data[1:]:
        matrix[i][v - 1] = 1

for row in matrix:
    print(" ".join(map(str, row)))
