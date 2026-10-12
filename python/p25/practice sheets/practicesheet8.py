##DATE:->21/09/2026
##Q1.PRINT SQUARES
"""n=int(input("enter the range of numbers:->"))
for i in range(1,n+1):
    print(i**2,end=" ")"""

##Q2.MULTIPLE OF 5
"""n=int(input("enter the range of numbers:->"))
for i in range(1,n+1):
    if i%5==0:
        print(i,end=" ")"""
        
##Q3.COUNT EVEN NUMBERS
"""n=int(input("enter number to count:->"))
for i in range(n+1):
    if i%2==0:
        print(i,end=" ")"""
        
#Q4.SUM OF EVEN NUMBERS
"""n=int(input("enter your number"))
a=0
for i in range(n+1):
    if i%2==0:
        a+=1
        continue
print(a)"""

#Q5.REVERSE COUNTING WITH EVEN NUMBERS
"""n=int(input("enter number:-"))
for i in range(n,-1,-1):
    if i%2==0:
        print(i)
        continue"""
        
#Q6.
"""p= 0
neg=1
n=int(input("enter how many integer you need check:->"))
print("enter your numbers:->")
for i in range(1,n+1):
    a=int(input(f"{i}."))
    if a>=0:
        p+=1
    else:
        neg+=1
print(f"your positive numbers are :->{p}")
print(f"your negative numbers are :->{neg}")"""

#Q7.
"""
a,c=0,0
n=input("enter your word:->")
for i in n:
    if i in "aeiouAEIOU":
        a+=1
    else:
        c+=1
print(f"the total vowel is {a}\n and the total consonant is {c}")"""

#Q8.
"""c=0
a=input('enter your word:->')
b=input("enter the letter you want to check:->")
if len(b)==1:
    for i in a:
        if i==b:
            c+=1
print(f"your letter repeats {c} times")"""

