
##question1:->find the pair with the given sum
##find all pairs of elements whose sum quuals a given target
##Example:
##input :[2,4,3,5,7,8]
##target :10
##output:
##(2,8)
##(3,7)

"""n = [2,4,3,5,7,8,]
target = 10
arr = len(n)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])"""

##Question : check whether a List is a sublist of another List
##write a python prigtam to check whether all element of one list appear consecutively in another list,
##Example:
##input:
##arr= [10,20,30,40,50]
##sub = [20,30,40]
##output:
##sublist found
##itself
arr= [10,20,30,40,50]
sub = [20,30,40]
found = False
for i in range (len(arr)):
    if arr[i:i+len(sub)] == sub :
        found = True
        break

if found:
    print("Sublist Found")

else:
    print("Not Found")
arr= [10,20,30,40,50]
n = len(arr)
sub = [20,30,40]
m = len(sub)

for i in range(0,n-m+1):
    if arr[i:i+m] == sub:
        print("SUBLIST FOUND")
        break
else:
    print("NOT FOUND")


##Question: Rotate a List to the Right by K Positions
##Write a Python program to rotate a list to the right by K positions
##using a loop.
##Example:
# Input:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Output:
# [4, 5, 1, 2, 3]
arr = [1, 2, 3, 4, 5]
k = 2



##Question: Sort a List in Ascending Order
##Write a Python program to sort the elements of a list in
##scending order without using the built-in sort() method.
##Example:
##Input:  [64, 34, 25, 12, 22, 11, 9]
##Output: [9, 11, 12, 22, 25, 34, 64]
arr = [64,34,25,12,22,11,9]
n  = len(arr)

for i in range(n):
    for j in range(n-1-i):
       
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
arr = [64,34,25,12,22,11,9]
n  = len(arr)

for i in range(n):
    for j in range(n-1-i):
        
        if arr[j] > arr[j+1]:
             arr[j],arr[j+1]= arr[j+1],arr[j]
print(arr)
