num_computer, num_participant = map(int, input().split())
computers = list(map(int, input().split())) 
for _ in range(num_participant):
    for j in range(len(computers)-1):
        if computers[j]>computers[j+1]:
            computers[j], computers[j+1] = computers[j+1],computers[j]

print(computers[-(num_participant)])