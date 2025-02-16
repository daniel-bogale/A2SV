password = input()
N = int(input())
start_found = False
end_found = False
for i in range(N):
    bark = input()
    if bark == password:
        start_found = True
        end_found = True
        break
    if bark[1] == password[0]:
        start_found = True
    if bark[0] == password[1]:
        end_found = True
    if start_found and end_found:
        break
print("YES" if start_found and end_found else "NO")