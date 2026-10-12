#sum of digits of a number 
"""# 123 1+2+3=6
n=int(input("enter number:")) #123
#while <condition >: for ex  while is used when we know ki kis condition
# tak loop run karana hai 
sum=0
while n!=0:
    # maths n/10 ex 123/10 =12.3
    # 123//10=12  (floor division - it removes the decimal part )
    # 123%10= 3
    sum+=n%10 #sum=sum+ n%10
    n=n//10  # to reduce the last value 
print(sum)"""
    
##use of try and except
"""try:
    n=int(input("enter number:"))
    for i in n:
        print(n%10)
except TypeError :
    print("this code doesnt work ")"""
    
## sum of digits of given number using for loop 
"""n=(input("enter your value:"))
s=0 #sum
for i in n:
    s+=int(i)
print(s)
"""
## if said that input is  in for m of integer 
"""n=int(input("enter your value:"))
s=0
for i in str(n):
    s+=int(i)
print(s)"""

##ATM pin verification system using while loop with errorhandling
"""print("welcome to krish jain ATM:-\n enter your pin\n remember you have only 3 tries and\n if you tried any cheating then your tries ends intantly ")
tries=3
try:
    while tries>0:
        n=(input("Pin:"))
        if len(n)==4 and n==1234: 
            print("Access granted\nwelcome to your account")
            break
        elif len(n)==4 and n!=1234:
            tries=tries-1
            if tries>0: 
                print(f"incorrect pin\nyou have only {tries} Tries left")
            elif tries==0:
                print("card blocked\n contact to your bank")
        else:
            print("pin is in between 0000 and 9999")
except ValueError:
    print("are you idiot!!! enter a valid entry")"""


    



    