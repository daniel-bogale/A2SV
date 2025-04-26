t = int(input())
for _ in range(t):
    arr = list(input().split())
    print(''.join([i[0] for i in arr]))