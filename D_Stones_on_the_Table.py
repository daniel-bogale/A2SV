_= int(input())
s = input()
previous_char = ""
count = 0
for i, val in enumerate(s):
    if(val == previous_char):
        count +=1
    previous_char = val
    
print(count)
    
    