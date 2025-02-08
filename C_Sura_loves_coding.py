N = int(input())
word = list(input())
ans = [0 for i in range(N)]
pointer = N - 2
is_reversed = False  
for i in range(N):
    ans[i] = word[pointer]
    if pointer == 0:
        is_reversed = True
        if N % 2 == 0:
            pointer = 1
        else:
            pointer = 2
    elif not is_reversed and pointer - 2 == -1:
        pointer = 0
    elif is_reversed:
        pointer += 2
    else:
        pointer -= 2

print("".join(ans)) 
