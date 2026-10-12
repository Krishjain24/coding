## function 
#they are of 2 types  1. user defined 2.inbuilt

"""#parameters and arguments
#whenever we want to accept a value in a function you have to use parameters
def addition(a,b): #parameters
    print(a+b)
#and whenever you want to provide value to those parameters you have to use arguments 
addition(12,12) #positional arguments 
addition(10,20)
"""
##return
"""def hello():
    return "how are you"
hello()
print(hello())"""

## print all the strong number between 1 to 100000
"""def strongnumber(a):
    temp=a
    sum=0
    while a!=0:
        fact=1
        for i in range(1,a%10+1):
            fact=fact*i
        sum=sum+fact
        a=a//10
        if temp== sum:
            print(temp)
            
for i in range(1,1000001):
    strongnumber(i)"""

##types of parameters and arguments 
#default -> we have to provide a default value to our parameters but it cannot be created before a normal parametes  
"""def addition(a,b,c,x=10,y=10):
    print(x+y)
    print(a+b)
    
addition(10,20,30)
addition()
   """
#positional vs default function
def xyz(a,b):
    print(a,b)

xyz(45,12) #positional arguments
xyz(b=12,a=45) 


