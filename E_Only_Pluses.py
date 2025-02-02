num_of_tests = input()
for _ in range(int(num_of_tests)):
    num_array = list(map(int,input().split()))
    
    for _ in range(5):
        current_min = min(num_array)
        current_min_index = num_array.index(current_min)
        
        num_array[current_min_index] +=1
        
    a, b, c = num_array
    print(a* b* c)
    
