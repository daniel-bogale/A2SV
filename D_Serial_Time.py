from collections import deque

k, n, m = map(int, input().split())
layers = []
for _ in range(k):
    layer = []
    while len(layer) < n:
        line = input().strip()
        if line:
            layer.append(line)
    layers.append(layer)

coords = []
while not coords or len(coords) < 2:
    line = input().strip()
    if line:
        coords = line.split()
x, y = map(int, coords)
x -= 1  
y -= 1

visited = [[[False for _ in range(m)] for __ in range(n)] for ___ in range(k)]
directions = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

count = 0
q = deque()
if layers[0][x][y] == '.':
    q.append((0, x, y))
    visited[0][x][y] = True
    count += 1

while q:
    l, i, j = q.popleft()
    for dl, di, dj in directions:
        nl = l + dl
        ni = i + di
        nj = j + dj
        if 0 <= nl < k and 0 <= ni < n and 0 <= nj < m:
            if not visited[nl][ni][nj] and layers[nl][ni][nj] == '.':
                visited[nl][ni][nj] = True
                count += 1
                q.append((nl, ni, nj))
print(count)