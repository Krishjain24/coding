##operators 
#arithmetic operator(+,-,*,/,//,%,**)
a=20 
b=30


"""print(a+b) #50 
print(a-b) #10
print(a*b) #600
print(20/5) #4.0 taken as float 
print(20//5) #4 it will remove the value after decimal 
print(5**2) # 25 exponential
print(62%5) # 2 remainder """

###Q1 take interst of principal ,rate and time and find out the simple interst # formula is (PRT/100)
""" method 1
a= int(input("principal:"))
b=float(input("rate:"))
c= int(input(" time:"))
si =(a*b*c)/100 
print (f"your simple intrerst is{si}")"""

""" method 2 
a= int(input("principal:"))
b=float(input("rate:"))
c= int(input(" time:"))
print(f"your simple intrerst is{(a*b*c*)/100}")
"""
### Q2 calculate compound interst 
"""a= int(input("principal:"))
b=float(input("rate:"))
c= int(input("time:"))
print (f"your compound interst is {(a*(1+(b/100))**c)-a} and your simple interst is{(a*b*c)/100}")"""


#assignment operator
a=10
a +=20
a-=30
a+=10
a//=2
a*=2
print(a)