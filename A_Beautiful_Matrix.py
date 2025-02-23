matrix = []
index_of_one = (0,0)
for i in range(5):
    current_row = list(map(int,input().split()))
    for idx,value in enumerate(current_row):
        if value == 1:
            index_of_one = (i,idx)
    matrix.append(current_row)
print(abs(2-index_of_one[0])+ abs(2-index_of_one[1]))