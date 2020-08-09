import random as ra 
import math 
all_nos = list()
for i in range(1, 101):
    all_nos.append(i)
#print(all_nos)
used_nos = list()
def ranno():
    a = ra.randrange(all_nos)
    used_nos.append(a)
    all_nos.remove(a)
    print("The next number is: ",a)
def noleft():
    print("A total of", range(all_nos), " numbers have not been called out. \n These are: ", all_nos)
def nosnotleft():
    print("A total of ", range(used_nos), " have been called out. /n These are: ", used_nos)
inp = input("What do you want to do ?")
if inp == "Next Number":
    ranno()
elif inp == "Numbers not called yet":
    nosnotleft()
elif inp=="Numbers already called yet":
    noleft()



