N = int(input())
for _ in range(N):
    length = int(input())
    requirements = list(map(int, input().split()))
    size = int(input())

    for _ in range(size):
        women = input()
        num_to_char = {}  
        char_to_num = {}  
        matched = "YES"

        if len(women) != length:
            matched = "NO"
        else:
            for i in range(length):
                num = requirements[i]
                char = women[i]

                if num in num_to_char:
                    if num_to_char[num] != char:
                        matched = "NO"
                        break
                else:
                    num_to_char[num] = char

                if char in char_to_num:
                    if char_to_num[char] != num:
                        matched = "NO"
                        break
                else:
                    char_to_num[char] = num

        print(matched)
