from collections import Counter

s1 = input()
s2 = input()

cnt = Counter(ch for ch in s1 if ch != ' ')  # count only non-space
ok = True
for ch in s2:
    if ch == ' ':
        continue
    cnt[ch] -= 1
    if cnt[ch] < 0:
        ok = False
        break

print("YES" if ok else "NO")