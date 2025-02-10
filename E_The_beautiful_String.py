if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word = input()
        seq = "1100"
        count = word.count(seq)
        str_word = list(word)

        q = int(input())
        for _ in range(q):
            i, v = input().split()
            i = int(i) - 1

            before_change = "".join(str_word[max(0, i - 3) : i + 4]).count(seq)
            str_word[i] = v
            after_change = "".join(str_word[max(0, i - 3) : i + 4]).count(seq)
            count += after_change - before_change

            print("YES" if count > 0 else "NO")