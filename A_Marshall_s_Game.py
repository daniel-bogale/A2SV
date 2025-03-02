N = int(input())
difficultyLevel  = "EASY"
levels = list(map(int,input().split()))

for val in levels:
    if val:
        difficultyLevel="HARD"
        
print(difficultyLevel)