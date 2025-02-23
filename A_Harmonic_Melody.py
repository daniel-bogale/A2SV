N=int(input())
for i in range(N):
    melody_len = int(input())
    melodies = list(map(int, input().split()))
    previous = melodies[0]
    is_perfect = True
    for idx in range(1,melody_len):
        if abs(previous-melodies[idx]) != 5 and abs(previous-melodies[idx]) != 7:
            is_perfect = False
            break
        previous = melodies[idx]
    print("YES" if is_perfect else "NO")