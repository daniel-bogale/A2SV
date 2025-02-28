N = int(input())
chat_history = {}

for i in range(N):
    chat_history[input()] = i

for person in sorted(chat_history, key=chat_history.get, reverse=True):
    print(person)