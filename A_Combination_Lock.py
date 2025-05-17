n = int(input())
state = list(map(int,input()))
password = list(map(int,input()))
count = 0
for i in range(n):
    diff = abs(password[i] - state[i])
    count += min(diff, 10 - diff)

print(count)