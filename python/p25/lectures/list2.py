##practicesheet by dhruv bhaiya 
## reverse the given list by two pointer approach
#1. for even
"""l=[10,20,30,40,50,60]
temp=len(l)-1
for i in range(0,len(l)//2):
    l[i],l[temp]=l[temp],l[i]
    temp-=1
print(l)"""

"""arr=[10,20,30,40,50,60]
n=len(arr)
for i in range(0,n//2):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
print(arr)

"""

##Question 2
""" l=[10,-5,20,-3,0,8]
for i in range(0,len(l)):
    a=l[i]
    if a>0:
        print("positive",a,)
    elif a<0:
        print("negative",a,) """
        
""" list=[10,-5,20,-3,0,8]
print("positive:",end=" ")
for i in range(len(list)):
    element=list[i]
    if element>0:
        print(f"{element}",end=" ")
print("negative:",end="")
for element in list:
    if element <0:
        print(f"{element}") """
        
"""l=[10,20,0,8]
sum=0
for i in range(len(l)):
    a=l[i]
    sum+=a
print(f"average is {sum/len(l)}")"""
    
"""l=[10,20,0,8]
sum=0
for i in list:
    sum+=i
print(f"mean:->{sum/len(list)}")"""

""" l=[2,96,69,77,145,20] 
g=l[0] #assumed max value
index=0
for i in range(len(l)):
    a=l[i]
    if a>g:
        g=a
        index=i
print(f"your greatest one is {g} and index is{index}") """