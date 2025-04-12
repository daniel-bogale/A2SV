t= int(input())
for _ in range(t):
    length = int(input())
    arr = list(input())
    problems_solved = set()
    count = 0
    for char in arr:
        if char not in problems_solved:
            problems_solved.add(char)
            count+=2
        else:
            count+=1
    print(count)