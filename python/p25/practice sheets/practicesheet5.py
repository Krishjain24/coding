##DATE->17/09/2026
##Q1. E- commerce return system
"""d=8
a=int(input("Enter product category:-\n 1. Electronics\n 2.clothing\n 3.food\n:-> ")) #
b=int(input("enter your date of purchase:-\n:->"))
c=int(input("is product opened?\n1. opened \n2.closed\n:->"))
if a in range(1,4):
    if b in range(8,32):
        if c in range(1,3):
            if a==1:
                if b< d+7:
                    if c==2:
                        print("Return accepted")
                    else:
                        print("return depend on condition")
                else:
                    print("return period expired")
            elif a==2:
                if b<d+15:
                    if c==2:
                        print("Return accepted")
                    else:
                        print("return depend with condition")
                else:
                    print("return period expired")
            elif a==3:
                print("food items can\'t be returned or replaced")
            else:
                print("select any option between 1 and 3 ")"""

##Q2.
"""a=int(input("enter your age:->"))
b=int(input("do you have a learner license:->"))                
c=int(input("did you passed the  driving test:->"))
if a in range(0,101):
    if b in range(1,3):
        if c in range(1,3):
            if a>=18:
                if b==1:
                    if c==1:
                        print("license appproved")
                    else:
                        print("retake driving test")
                else:
                    print("get learner license first")
            else:
                print("you are not eligible")
        else:
            print("choose from the given option")
    else:
        print("choose from the given option")
else:
    print("choose from the given option")"""

##Q3.
"""a=int(input("select plan type:-\n 1.basic\n 2.premium\n:->"))
b=int(input("data usage(in GB):-"))
c=int(input("auto renewal:->\n 1. yes \n 2. no \n :->"))
if a in range(1,3):
    if c in range(1,3):
        if a==1:
            if b <=100:
                print("price is 499₹")
            elif b>300:
                if c==1:
                    print("price is 599₹")
                else:
                    print("upgrade to premium")
        if a==2:
            if b <=300:
                if c==1:
                    print("price is 799₹")
                else:
                    print("price is 849₹")
            elif b>300:
                print("premium limit exceeded")
        else:
            print("select a  valid option")
    else:
        print("select a  valid option")
else:
    print("select a  valid option")
"""

##Q4.restaurant table booking:->
a=int(input("number of guest:->"))
b=int(input("table type:\n 1.normal \n 2.private\n :->"))
c=int(input("special occasion:_\n 1.yes\n 2. no\n :->"))
if a in range (1,21):
    if b in range(1,3):
        if c in range(1,3):
            if b==1:
                if a<=6:
                    print("booking available")
                else:
                    print("booking not available")
            if b==2:
                if a<=10:
                    if c==1:
                        print("private table with decoration booked")
                    else:
                        print("private table booked")
                else:
                    print("maximun 10 guest allowed")

##Q5.
"""a=int(input("enter percentage:-"))
b=int(input("enter family income(in lakhs):-"))
c=int(input(" is there anny sports achivement:->\n 1.yes\n2.no\n:->"))
if a in range(1,101):
    if b>1:
        if c in range(1,3):
            if a>=80:
                if b<=3:
                    print("full scholarship")
                else:
                    if c==1:
                        print("partial scholarship")
                    else:
                        print("no scholarship")
            elif a in range(60,80):
                if c==1:
                    print("sports scholarship")
                else:
                    print("no scholarship")
            else:
                print("not eligible for scholarship")
        else:
            print("enter valid value")
    else:
        print("enter valid value")
else:
    print("enter valid value")"""



            

                    