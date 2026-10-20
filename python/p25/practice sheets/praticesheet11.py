##DATE:->24/09/26
##que 1.
"""even,odd=0,0
n=int(input("enter your range of numbers:->"))
for i in range(n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
if even>odd:
    print(f"the diff between the sum of even and odd is{even-odd}")
else:
    print(f"the diff between the sum of even and odd is{odd- even}")"""

##que 2.
"""large=0
n=int(input("enter the numbers you want to compare:-> "))
print("enter your number:->")
for i in range(1,n+1):
    e=int(input(f"value {i}.=")) 
    if e>large:
        large=e
print(large)"""

##que 3
"""n=int(input("enter your numbers:->"))
pno=None
for i in range(n):
    e=int(input(f"{i+1}."))
    if pno!=None:
        if pno>e:
            pno=e     
    elif pno==None:
        pno=e
print(f"smallest number is:-> {pno}")"""

##Que 4.
#m1.only if zero is in last
"""count=0
n=int(input("enter your number:->"))
for i in range(n):
    e=int(input(f"{i+1}."))
    if e%10==0:
        count+=1
print(f"total numbers which contain the digit zero in last  are :{count}")
"""
#m2- if zero is in somewhere in the number
#try 1
"""n=int(input("enter your number:->"))
totalZero=0
for i in range(n):
    e=int(input(f"enter the number:->{i+1}."))
    zeroCount=str(e).count("0")
    totalZero+=zeroCount
    print(f"the number of zero in this number {i+1}.{e}is:{zeroCount}")
print(f"the total zero in all enteries is:{totalZero}")
"""
#try 2 ## by function

##Que 5.->
##method 1 . without using for loop vs
"""n=int(input("enter your number:->"))
l=len(str(n))
n=str(n)
if n[0]==n[l-1]:
    print("both are same ")
else:
    print("both are not same")"""

#method 2.- 
#by using the "map()" and the "*_" 

"""n=(input(f"enter your number:->"))
f,*_,l=map(int,n)                      
if f==l:
    print("same")
else:
    print("not same")"""

