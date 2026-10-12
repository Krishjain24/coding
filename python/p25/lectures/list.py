##list methods
"""l=[]
print(dir(list)) # to know all type of methods 

l.sort()
print(l)"""
    
"""help(list)"""  # to know all function with methods 

## list methods 
l=[10,20,30,40]
# 1. append 
"""l.append(50)
print(l)"""

#2.copy
"""b =l
l[0] =1000
print(b)"""

"""b =l.copy()
l[0] =1000
print(b)
print(l)"""

#3.count
"""a=[1,1,1,1,1,1,1,2,2,2,2,2,2,]
print(a.count(1))"""

##Q1.
"""a=[10,20,30,40,50]
b=[]
for i in range (len(a)-1,-1,-1):
    b.append(a[i])
print(b)
"""

a=[10,20,30,40,50,60,70,80,90,100]
temp=len(a)-1
for i in range(0,len(a)//2-1):
    a[i],a[temp]=a[temp],a[i]
    temp=temp-1
print(a)