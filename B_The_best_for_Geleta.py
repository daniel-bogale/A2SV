N = int(input()) 

for _ in range(N):
    array_len, test_len = map(int, input().split())  
    arr = list(map(int, input().split())) 
    answer = []

    for _ in range(test_len):
        opp, start, end = input().split()
        start, end = int(start), int(end)  
        for i in range(array_len):
            if start <= arr[i] <= end:  
                if opp == "+":
                    arr[i] += 1
                else:
                    arr[i] -= 1

        answer.append(max(arr))  
    
    print(" ".join(map(str, answer))) 
