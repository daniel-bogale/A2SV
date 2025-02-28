# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

N = int(input())
chat_history = {}

for i in range(N):
    chat_history[input()] = i

for person in sorted(chat_history, key=chat_history.get, reverse=True):
    print(person)