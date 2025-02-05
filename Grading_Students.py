N = int(input())
for _ in range(N):
    num = int(input())
    next_grade = 5*(num//5)+5    
    if (num >= 38 and next_grade != num and next_grade-num < 3):
        print(next_grade)
    else:
        print(num)