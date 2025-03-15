t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def check_exist(i, j):
        return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

    def is_val_stranger(i, j, value):
        for x, y in dirs:
            current_row = i + x
            current_col = j + y
            if check_exist(current_row, current_col) and matrix[current_row][current_col] == value:
                return False
        return True

    val_stranger_dict = {}
    count_val = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            isStranger = is_val_stranger(i, j, value)
            if isStranger:
                val_stranger_dict[value] = True
            else:
                val_stranger_dict[value] = False

            count_val[value] = count_val.get(value, 0) + 1

    unique_values = set(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])))

    steps = 0
    max_freq_value = -1
    max_freq = -1

    for value in unique_values:
        if count_val[value] > max_freq:
            max_freq_value = value
            max_freq = count_val[value]

        if val_stranger_dict[value]:
            steps += 1
        else:
            steps += count_val[value]
    if max_freq == -1:
        steps -= 1
    else:
        steps -= max_freq
    print(steps)