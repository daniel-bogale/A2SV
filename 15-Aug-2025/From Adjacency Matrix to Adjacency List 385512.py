# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(n):
    adj = []
    for j in range(n):
        if matrix[i][j] == 1:
            adj.append(j + 1)
    print(len(adj), *adj)