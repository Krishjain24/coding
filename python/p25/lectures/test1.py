##1. **Prime Numbers from 1 to N (10 marks)**
    
#Take a positive integer N as input and print all prime numbers from 1 to N (inclusive).
"""n=int(input("enter number:->"))
for j  in range(1,n+1):
    for i in range(2,j+1):
        if j%i==0:
            break
        else:
            print(f"{j} is prime")
            break"""

##Q2.
"""new=0
n=int(input("enter your number:->"))
temp=n
while n!=0:
    fact=1
    a=0
    a=n%10
    for i in range(1,a+1):
        fact=fact*i
    new=new + fact
    n=n//10
if new== temp:
    print("strong number")
else:
    print("not a strong number")"""
    
##Q3.
"""m=input("enter number:->")

length=len(m)
temp=m
sum=0
n=int(m)
while n!=0:
    a=n%10
    sum=sum*10+a**length
    n=n//10
if sum==temp:
    print("armstrong number")
else:
    print("not a armstrong number")"""
    
##Q5.
"""n=int(input("enter number:->"))
temp=n
new=0
while n!=0:
    a=n%10
    new=new*10+a
    n=n//10
if temp==new:
    print("palindrome")
else:
    print("not a palindrome")"""
    
##Q4.
large=0
large2=0
n=int (input("enter the number:"))
while n!=0:
    a=n%10
    n=n//10

