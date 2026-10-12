## STRONG NUMBER
"""n=int(input("enter number:-"))
sum=0
temp=n
while n!=0:
    z=n%10
    fact =1
    for i in range(1,z+1):
        fact*=i
    sum=sum +fact
    n=n//10
if sum==temp:
    print("strong number")    
else:
    print("not a strong  number")"""
    
##NUMBER GUESSING GAME(1-100)
import random
num=random.randint(1,100)
tries=0
while True:
    tries+=1
    guess=int(input("guess your number between 1-100:"))
    if guess==num:
        print(f"congratulation you won in {tries} tries")
        break
    elif guess>num:
        print("Go a bit lower")
    else:
        print("Go a bit higher")
        