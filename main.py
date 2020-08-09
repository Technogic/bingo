import random as ra 
import math 
all_nos = list()
for i in range(1, 101):
    all_nos.append(i)
print(all_nos)
used_nos = list()
def ranno():
    a = ra.randrange(1,101)
    if a not in all_nos:
        ranno()
    else:
        pass
    used_nos.append(a)
    all_nos.remove(a)
    print("The next number is: ",a)
def noleft():
    print("The numbers have not been called out are :"+ all_nos)
def nosnotleft():
    print("The numbers that have been called out are: ", used_nos)
inp = input("What do you want to do ? ")
if inp == "Next Number":
    print(ranno())
elif inp == "Numbers not called yet":
    print(nosnotleft())
elif inp=="Numbers already called yet":
    print(noleft())
else:
    print("Invalid Command")




