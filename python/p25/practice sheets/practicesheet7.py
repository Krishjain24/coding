#Date-19/06/26
##Q1.
"""n=int(input("enter your age:->"))
if n in range(1,101):
    if n<18:
        print("you are not eligible for NEET")
    else:
        print("you are eligible for NEET")"""
        
##Q2.
"""a=1000000
n=float(input("enter amount to withdraw:-"))
if n<a:
    print("Insufficient balance")
else:
    print("you can withdraw your amount")"""
    
##Q3.
"""n=float(input("enter temperature"))
if n in range(-273.15,373.15):
    if n<30:
        print("cold temp")
    else:
        print("hot temp")"""

##Q4.
"""n=int(input("enter marks:->"))
if n in range():
    if n<50:
        print("failed")
    else:
        print("passed")"""

##Q5.
"""n=int(input("enter pin:->"))
if n in range(00000,99999):
    if n==12345:
        print("correct password")
    else:
        print("wrong password")
else:
    print("enter 5 digit pin!!!")
"""

##Q6.
"""n=float(input("enter amount:->"))
if n>=2000:
    print("you are eligible for discount")
else:
    print("you are not eligible for discount")"""

##Q7.
"""n=int(input("enter number:->"))
if n<0:
    print("negative")
else:
    print("positive")"""

##Q8.
"""n=int(input("enter your attendence:->"))
if n in range(1,101):
    if n>=75:
        print("you are eligible for for end sem")
    else:
        print("you are not eligible")
else:
    print("enter valid attendence")"""

##Q9.
"""tries=0
invalidtry=0
cheat=0
while True:
    try:
        n=int(input("enter your pin:->"))
        if n in range(0000,9999):
            if n==9999:
                print("Access granted")
                break
            else:
                print("incorrect pin\n try again")
                tries+=1
        else:
            print("pin is in between 0000 and 9999")
            invalidtry+=1
        if tries==3:
            print("you have tried more than 3 times\n acces denied")
            break
        if invalidtry==3:
            print("you are just playing with system\n account blocked")
            break
    except ValueError:
        print("enter integer as your pin")   
        cheat+=1
    if cheat==3:
        print("you are trying to cheat with system")"""


##Q10.
"""n=int(input("enter amount:->"))
if n<=1000:
    print("delivery charges applied")
else:
    print("free delivery")"""
        
         




