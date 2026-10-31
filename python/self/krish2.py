
"""l,u=0,0
n=input("enter word:->")
if n.isalpha():
    for i in n:
        if n.islower():
            l+=1
        elif n.isupper():
            u+=1
    print(f"uppercase:{u}& lowercase:{l}")"""
            
## check the no of uppercase and lowercase letters in a string
"""n=input("enter word:->")
l,u=0,0
if n.isalpha():
    for i in n:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
    print(f"uppercase:{u}& lowercase:{l}")"""
    
"""n=input("enter word:->")
l,u=0,0
large,small=str(),str()
if n.isalpha():
    for i in n:
        if i.islower():
            small=small+ i
        elif i.isupper():
            large=large+ i
    print(f"uppercase:{large}& lowercase:{small}\nuppercase:{len(large)}& lowercase:{len(small)}")"""

n=int(input("enter your number:->"))


