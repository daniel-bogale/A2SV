string = input()
prev = []
for char in string:
    if len(prev) > 0 and char == prev[-1]:
        prev.pop()
    else:
        prev.append(char)
print(''.join(prev))