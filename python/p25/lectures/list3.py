##que 1. find the missing number:->(condition- only one number is missing)
"""l=[1,2,3,5,6,7]
esum=0
asum=0
n=len(l)
for i in l:
    asum=((n+1)(n+2))/2
    esum+=i
print(f"the element missing is{asum-esum}")"""

"""arr=[1,2,4,5]
n=len(arr)
og_n=n+1
#og_sum =((og_n)*(og_n+1))//2
og_sum=0
for i in range(1,og_n+1):
    og_sum+=1
real_sum=0
for elem in arr:
    real_sum+=elem
missing=og_sum-real_sum
print(missing)"""

##Q2.check list is sorted in assending order 
"""l=[10,20,30,40,50]
n=len(l)
for i in range(n):
    if l[i]<l[i+1]:
        print("sorted")
        break
else:
        print("not sorted")"""
        


##Q3.check list is sorted in desending  order
"""l=[10,20,30,40,50]
n=len(l)
for i in range(n):
    if l[i]>l[i+1]:
        print("sorted")
        break
else:
        print("not sorted")"""

##Q4. check if the list is sorted(able to fulfill both condition assending and decending)
"""l=[10,20,30,40,50,60]
n=len(l)
for i in range(n):
    if l[i]<l[i+1]:
        print("sorted in assending order")
        break
    elif l[i]>l[i+1]:
        print("sorted in desending order")
        break
"""

l=[1,2,3,3,2,1]
for i in range(len(l)):




