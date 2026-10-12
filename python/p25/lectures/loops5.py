#find the highest common factor 
"""a=int(input("tell 2 numbers:"))
b=int(input())
if a>b:
    for i in range(b,0,-1):
        if b%i==0 and a%i==0:
            print(f"HCF is {i}")
            break
elif b>a:
    for i in range(a,0,-1):
        if b%i==0 and a%i==0:
            print(f"HCF is {i}")                  
            break
else:
    print(f"Both are equal and The HCF is {a}")"""  

##seperate the digits of 5379
a=int(input("tell the number"))
while a> 0:
    print(a%10)
    a=a//10
    
