N = int(input())
points = list(map(int, input().split(" ")))
prizes = list(map(int, input().split(" ")))

def find_big_price(point):
    quantities=[]
    indexes = []
    for idx in range(len(prizes)-1,-1,-1):
        prize = prizes[idx]
        if point>=prize:
            quantity = point//prize
            quantities.append(quantity)
            indexes.append(idx)
            point-= quantity*prizes[idx]
    return [indexes,quantities,point]
            

remaining = 0
rewards = [0]*len(prizes)
for point in points:
    current_total_point = remaining+ point
    indexes, quantities,remaining = find_big_price(current_total_point)

    for i in range(len(indexes)):
        rewards[indexes[i]] += quantities[i]

print(" ".join(map(str, rewards)))
print(remaining)