t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
 
    visited = [[False] * m for _ in range(n)]
    max_vol = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                vol = 0
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    vol += matrix[x][y]
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if matrix[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                max_vol = max(max_vol, vol)
    print(max_vol)