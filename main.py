import random as ra 
import math 
all_nos = list()
for i in range(1, 101):
    all_nos.append(i)
print(all_nos)
used_nos = list()
def ranno():
    a = ra.randrange(1,101)
    if a in used_nos:
        ranno()
    else:
        pass
    used_nos.append(a)
    all_nos.remove(a)
    print("The next number is: ",a)
def nosnotleft():
    print("The numbers that have been called out are: ", used_nos)
def noleft():
    print(all_nos)
for i in range(10):
    inp = input("What do you want to do ? ")
    if inp == "Next Number":
        inp2 = int(input("How many numbers you want ?"))
        i = 0 
        for i in range(inp2):
            print(ranno())
            i += 1
    elif inp == "Numbers already called":
        print(nosnotleft())
    elif inp == "Numbers not called yet":
        print(noleft())
    elif inp == "Quit":
        break
    else:
        print("Invalid Command")
    