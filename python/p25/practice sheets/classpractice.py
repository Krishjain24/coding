##1st time
# Q1. 
"""n=int(input("enter number:-"))
for i in range(1,n+1):
    print(i)"""
#Q2.
"""n=int(input("enter number:-"))
for i in range(n,0,-1):
    print(i)"""
#Q3.
"""n=int(input("enter the number whose table you need to print:"))
print("your table is:")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")"""
#Q4.
"""n=int(input("enter number:"))
a=0
for i in range(1,n+1):
    a+=i
print(a)"""
#Q5.
"""n=int(input("enter number:"))
a=1
for i in range(1,n+1):
    a*=i
print(a)"""
#Q6.
"""//method1
n=int(input("enter number:-"))
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
print(n)"""
"""//method2
n=int(input("enter number:-"))
for i in range(1,n+1):
    if n%i==0:
        print(i)"""
#Q7.
"""n=int(input("enter number:-"))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
print(a)"""
#Q8.
"""n=int(input("enter your number:-"))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
if a==2:
    print("prime")
else:
    print("composite")"""
#Q9.
"""n=int(input("enter number:"))
for i in range(2,n):
    if n%i==0:
        print("composite")
        break
else:
    print("prime")"""

#Q10.
"""n=int(input("enter number:-"))
for i in range(2,n//2+1):
    if n%i==0:
        print("composite:")
        break
else:
    print("prime")"""

#Q11.
"""n=int(input("enter number:"))
for j in range(2,n+1):
    for i in range(2,j//2+1):
        if n%j==0:
            print(f"{j} is composite")
            break
    else:
        print(f"{j} is prime")"""
        
#Q12.
"""a=int(input("enter number:"))
b=int(input("enter 2nd number:"))
if a>b:
    for i in range(b,0,-1):
        if a%i==0 and b%i==0:
            print(f"hcf is {i}")
            break
else:
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            print(f"hcf is {i}")
            break"""

#13.
#method 1.
"""n=int(input("enter number:-"))
while n!=0:
    print(n%10)
    n=n//10"""
#method 2.
"""n=int(input("enter number:-"))
for i in str(n):
    print(n%10)
    n=n//10"""
    
    
#14.
"""n=int(input("enter the number"))
a=0 #for calculating sum
while n!=0:
    a+=n%10
    n=n//10
print(a)"""
#method 2 
"""n=int(input("enter value:-"))
a=0
for i in str(n):
    a+=n%10
    n=n//10
print(a)"""

#15.
"""n=int(input("enter number:-"))
a=0
while n!=0:
    a=a*10 + n%10 
    n=n//10
print(a)"""

#16.
"""n=int(input ("enter number:-"))
c=n
a=0
while n!=0:
    a=a*10+n%10
    n=n//10
if c==a:
    print("palindrome number")
else:
    print("not a plindrome number")"""
    
#Q17.
"""n=int(input("enter number:-"))  
a=n # for saving n value   
sum=0
while n!=0:
    fact_b=1
    b=n%10
    n=n//10
    for i in range(1,b+1):
        fact_b*=i
    sum=sum + fact_b
if sum==a:
    print("strong number")
else:
    print("not a strong  number")"""
    
#Q18.
import random
a=random.randint(1,100)
tries=0
cheat=0
try:
    while True:
        n=int(input("guess number:-"))
        tries+=1
        if n==a:
            print (f"congratulation you guess the correct number in{tries} tries")
        elif n>a:
            print(" go a bit lower")
        else:
            print("go a bit higher")
except ValueError:
    cheat+=1
    print("enter number only ")
    if cheat==2:
        print("one more try and you will be  out  ")
    elif cheat==3:
        print(" this is  the last warning")

        




        
    
