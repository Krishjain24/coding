##DATE->22/09/26
#Q1.
"""p,a=0,0
print("enter your attendence:->")
for i in range(1,8):
    n=input(f"day {i}.:-> ")
    if n.isalpha():
        if n in "pP":
            p+=1
        elif n in "aA":
            a+=1
        else:   
            print("enter valid attendence")
            while True:
                n=input(f"day {i}.:-> ")
                if n in "pP" :
                        p+=1
                        break
                elif n in "aA":
                        a+=1
                        break
    else:
        print(f"enter valid entry\n "" this  type of entry is not allowed")
print(f"you were present for {p} days and absent for {a} days")"""




#Q2.
"""p,a=0,0
n=int(input('total number of product you want to inspect:->'))
print("inspection of product")
for i in range(1,n+1):
    ins=input(f"{i}.:->")
    if ins=="good":
        p+=1
    elif ins=="bad":
        a+=1
    else:
        print("enter valid entry")
print(f"your have {p} good products and {a} bad products")"""

#Q3.
"""g=str()
s=str()
sum=int()
print("enter your everyday saving(in ₹):->")
for i in range(1,8):
    n=int(input(f"day {i}:->"))
    sum+=n
    if n>500:
        g+=f" {i},"
    else:
        s+=f" {i},"
print(f"your total saving of the week is{sum}\n saving greater than 500 is on{g}th day \n ans smaller than 500 is on{s}th day")"""

#Q4.
"""g=str()
s=str()
sum=int()
print("enter your everyday electricity consumption(in kwh):->")
for i in range(1,8):
    n=int(input(f"day {i}:->"))
    sum+=n
    if n>10:
        g+=f" {i},"
    else:
        s+=f" {i},"
print(f"your total consumption of the week is{sum}\n consumption greater than 10 is on{g}th day \n and smaller than 500 is on{s}th day")
"""

#Q4.
"""p,a=int(),int()
days=["monday","tuesday","wednesday","thursday","friday","monday","tuesday","wednesday","thursday","friday"]
for i in range(1,11) and range(len(days)):
    n=input(f"{i+1}.Day:{days[i]}:->").lower()
    if n.isalpha():
        if n=="p":
            p+=1
        elif n=="a":
            a+=1
        else:
            print("enter valid attendence")
            while True:
                n=input(f"{i}.Day{days[i]}:->").lower()
                if n in "p" :
                        p+=1
                        break
                elif n in "a":
                        a+=1
                        break
    else:
        print(f"enter valid entry\n "" this  type of entry is not allowed")

ap=(p/(p+a))*100
if ap>=75:
    print(f"your total attendence is {ap}\n congratulation for having 75%+ attendence")
else:
    print(f"your total attendence is {ap}\n sorry you dont have 75%+ attendence")"""


    
        

        