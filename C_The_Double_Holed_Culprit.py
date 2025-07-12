n= int(input())
arr = list(map(int,input().split()))
result = []

for i in range(n):
    current_idx = i
    touched = {i+1}
    while True:
        val = arr[current_idx]
        if val in touched:
            result.append(val)
            break
        touched.add(val) 
        current_idx = val-1

print(" ".join(map(str,result)))
