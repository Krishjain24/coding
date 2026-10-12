def range(*args):
    print(args)
range(1,2,3)

def range(*args):
    if len(args)==1:
        a=(args)
range(1,2,3)
##recursion and backtracking 
#recursion
#print numbers from 1 to 30 without using for and while loop and multiple print function
def number(n):
    if n<=30:
        print(n)
        number(n+1)
number(1)
   
"""def number(n):
    print(n)
    if n==30:
        return
    number(n+1)
number(1)"""

# backtracking 
"""
def hello1():
    hello2()
    print("hello1")
def hello2():
    hello3()
    print("hello2")
def hello3():
    hello4()
    print("hello3")
def hello4():
    print("hello4")
hello1()
"""     
##
"""def number(n):
    if n==31:
        return 
    number(n+1)
    print(n)
number(1)  #output->30 to 1"""

##leetcode que 9 soln
# def isPalindrome( x) :
#         c=x
#         a=0
#         if x<0:
#             return False
#         if x>0:
#             while x!=0:
#                 a=a*10+x%10
#                 x=x//10
#             if a==c:
#                 return (True)
#             else:
#                 return False
# print(isPalindrome(121))      

        