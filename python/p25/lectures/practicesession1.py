##perfect number 
"""n=int(input("enter your numbers:"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("non perfect number")"""
     
##Q2.Fibonacci series upto n terms 
"""n=int(input("enter number"))
a=0
b=1
c=a+b
for i in range(n):
    c=a+b
    a=b
    b=c
print(a,end=" ")"""

##minimum currency notes breakdown
n=int(input("enter total amount:"))
a=0
while n!=0:
    if n//500>500:
        a+=1
        

    

    
    
    
    
    