n=int(input())
rat = []
woman_child = []
man = []
captain =[]
for i in range(n):
    [name, category] = input().split()
    if category == "rat":
        rat.append(name)
    elif category == "woman" or category == "child":
        woman_child.append(name)
    elif category=="man":
        man.append(name)
    else:
        captain.append(name)

all_value = rat + woman_child + man + captain

for val in all_value:
    print(val)