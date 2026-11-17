##DATE:->28/09/2026
##que1 
"""new=0
n=int(input("enter your number:->"))
while n!=0:
    a=n%10
    n=n//10
    new=new*10+a
print(new)"""

##que2
"""new=0
n=int(input("enter your number:->"))
check=n
while n!=0:
    a=n%10
    n=n//10
    new=new*10+a
if new==check:
    print("palindrome")
else:
    print("not a palindrome")
"""

##que 3.
"""count=0
n=int(input("enter your number to check:->"))
while n!=0:
    a=n%10
    n=n//10
    if a>=5:
        count+=1
print(f"total number which are greater than 5 are {count}")"""

##que 4
"""p=1
n=int(input("enter your value:->"))
while n!=0:
    a=n%10
    n=n//10
    p=p*a
print(f"the product of the digits is {p} ")
"""

##que 5.
"""n=int(input("enter your number:->"))
while n!=0:
    a=n%10
    n=n//10
    if a==7:
        print("present")
        break
else:
    print("not present")"""

##que 6.
""" count=0
n=int(input("enter your number:->"))
while n!=0:
    a=n%10
    n=n//10
    if a%3==0:
        count+=1
print(count) """

##que 7
""" n=(input("enter your number:->"))
len= len(n)
nn=0
for i in range(len):
    nn=nn*10+9
print(nn) """

##que8
""" n=int(input("enter your value:->"))
l=float("-inf")
l2=float("-inf")
while n!=0:
    a=n%10
    n=n//10
    if a>l:
        l2=l
        l=a
    elif a> l2:
        l2=a
print(l2) """

##que 9
""" n=int(input("enter your digit:->"))
while n!=0:
    a=n%10
    n=n//10
    if a%2!=0:
        print("not every digit is even!!!")
        break
else:
    print("every digit is  even") """

##que 10
""" n=int(input("enter your number:->"))
n=n//10
print(n) """




