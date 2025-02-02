first_word = input().capitalize()
second_word = input().capitalize()
if(first_word < second_word):
    print("-1")
    
elif(second_word < first_word):
    print("1")
    
else:
    print("0")