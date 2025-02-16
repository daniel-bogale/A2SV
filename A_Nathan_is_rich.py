N = int(input())
for i in range(N):
    num_of_wheels = int(input())
    print(num_of_wheels//4 + num_of_wheels%4//2)