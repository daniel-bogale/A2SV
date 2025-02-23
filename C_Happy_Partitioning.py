N = int(input())
def count_val(val, word):
    count = 0
    for char in word:
        if char == val:
            count += 1
    return count
for _ in range(N):
    length = int(input())
    word = input()
    left_zero_count = 0
    right_one_count = count_val("1",word)
    
    possible_places = []
    if right_one_count/length >= 0.5:
        possible_places.append(0)
            
    for idx, char in enumerate(word):
        if char == "1":
            right_one_count-=1
        else:
            left_zero_count+=1
        if left_zero_count/(idx+1) >= 0.5 and (length-idx-1 == 0 or right_one_count/(length-idx-1) >= 0.5):
            possible_places.append(idx+1)
    
    closest_to_center = possible_places[0]
    for val in possible_places:
        if abs(val-(length/2))< abs(closest_to_center-(length/2)):
            closest_to_center = val
    
    print(closest_to_center)