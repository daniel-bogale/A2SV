n, A, B = map(int, input().split())
holes = list(map(int, input().split()))

first_hole = holes[0]
remaining = sorted(holes[1:], reverse=True)  
total = sum(holes)
count = 0

for hole in remaining:
    if first_hole/total * A >= B:
        break 
    total -= hole 
    count += 1

print(count)