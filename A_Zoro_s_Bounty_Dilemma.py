N = int(input())
for _ in range(N):
    signs = input()
    current_relation = "="
    for sign in signs:
        if sign == ">":
            if current_relation == "=" or current_relation == ">":
                current_relation = ">"
            else:
                current_relation = "?"
                break
        elif sign == "<":
            if current_relation == "=" or current_relation == "<":
                current_relation = "<"
            else:
                current_relation = "?"
                break
    print(current_relation)