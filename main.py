import random as ra 
import math 
all_nos = list()
for i in range(1, 101):
    all_nos.append(i)
#print(all_nos)
used_nos = list()
def ranno():
    a = ra.randrange(1,101)
    if a in used_nos:
        ranno()
    else:
        pass
    used_nos.append(a)
    print("The next number is: ",a)
def nosnotleft():
    print("The numbers that have been called out are: ", used_nos)
inp = input("What do you want to do ? ")
if inp == "Next Number":
    inp2 = int(input("How many numbers you want ?"))
    i = 0 
    for i in range(inp2):
        print(ranno())
        i += 1
elif inp == "Numbers not called yet":
    print(nosnotleft())
else:
    print("Invalid Command")




