# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def check_exist(i, j):
        return 0 <= i < n and 0 <= j < m

    def is_val_stranger(i, j, value):
        for x, y in dirs:
            ni, nj = i + x, j + y
            if check_exist(ni, nj) and matrix[ni][nj] == value:
                return False
        return True

    val_stranger_dict = {}
    count_val = {}

    for i in range(n):
        for j in range(m):
            value = matrix[i][j]
            count_val[value] = count_val.get(value, 0) + 1
            if is_val_stranger(i, j, value):
                val_stranger_dict[value] = True
            else:
                val_stranger_dict[value] = False

    unique_values = set(count_val.keys())

    steps = 0
    max_freq_value = None
    max_freq = -1

    for value in unique_values:
        if val_stranger_dict[value]:
            steps += 1
        else:
            steps += count_val[value]
            if count_val[value] > max_freq:
                max_freq_value = value
                max_freq = count_val[value]

    # Ensure max_freq_value is valid before accessing the dictionary
    if max_freq_value is not None and val_stranger_dict.get(max_freq_value, False):
        steps -= 1
    elif max_freq_value is not None:
        steps -= max_freq

    print(steps)
