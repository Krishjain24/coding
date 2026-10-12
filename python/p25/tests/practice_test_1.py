"""
Practice Problems - Basic Programming
======================================
1. Count Numbers Divisible by 3 and 5
2. Check if a Number is Prime
3. Count the Number of Digits Using a Loop
4. Find the HCF Using a For Loop
"""


# ------------------------------------------------------------
# 1. Count Numbers Divisible by 3 and 5
# ------------------------------------------------------------
"""n=int(input("enter number:-"))
a=0
for i in range(1,n+1):
    if i%5==0 and i%3==0:
        a=a+1
print(a)"""









"""
    Counts how many numbers from 1 to `limit` (inclusive)
    are divisible by both 3 and 5 (i.e. divisible by 15).
    """


# ------------------------------------------------------------
# 2. Check if a Number is Prime
# ------------------------------------------------------------
"""
    Returns True if n is a prime number, False otherwise.
    """
"""n=int(input("enter number:-"))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
if a==2:
    print("true")        
else:
    print("false")"""
    


# ------------------------------------------------------------
# 3. Count the Number of Digits Using a Loop
# ------------------------------------------------------------

"""
    Counts the number of digits in an integer n (handles negatives too).
    """
"""a=int(input("enter number:-"))  
b=0 
while a>0:
    if a%10>0:
        b+=1
    a=a//10
print(b)"""


    

    


# ------------------------------------------------------------
# 4. Find the HCF (GCD) Using a For Loop
# ------------------------------------------------------------

"""
    Finds the HCF (Highest Common Factor / GCD) of two numbers
    using a for loop.
    """
"""n=int(input("enter values:-"))
m=int(input("enter values:-"))
for i in range(n+1,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break"""
    


