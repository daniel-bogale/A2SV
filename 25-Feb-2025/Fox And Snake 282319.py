# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

row, col = map(int, input().split())
answer = [["."]*col for i in range(row)]
for i in range(row):
    if i % 2 == 0:
        answer[i] = ["#"]*col
        continue
    elif i%4 == 1:
        answer[i][-1] = "#"
        continue
    else:
        answer[i][0] = "#"
        continue
for i in range(row):
    print(("").join(answer[i]))