# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

N = int(input())
chat_history = {
    
}
for i in range(N):
    person = input()
    chat_history[person] = (person,i)

history = [val for val in chat_history.values()]
history = sorted(history, key=lambda val: val[1],reverse=True)
for val in history:
    print(val[0])
