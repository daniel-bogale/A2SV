# Problem: Day-8: Dictionaries and Maps - https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

phone_book = {}
N = int(input())  
for i in range(N):
    key, value = input().split(" ")
    phone_book[key] = value

while True:
    try:
        name = input()
        phone_no = phone_book.get(name, "Not found")  
        if phone_no != "Not found":
            print(f"{name}={phone_no}")
        else:
            print(phone_no)
    except EOFError:
        break  