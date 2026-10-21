#########################################################################################
###########################LIST###########################################################
#----------------------------------------------------------------------------------------


#-------------------days3------------->

# a = [34,12,89,45,67,12,78,23]

#list

#1) () Tuples
#2) [] List
#3) {} Set ,Dictionary

#list

#Hetrogenous nature - you can store multiple Data Types eg:-

'''a = ["Akash",28,True,15.5,print]'''

#indexing - same as string

# #Mutsble Nature - you can change any value of your list

# l = [10,20,30,40,50]

# l[0] = 500
# print(l)

# #loops on list:

# l = [10,20,30,40,50,99,189,7,56]

# #loop on value
# for i in l:
#     if i % 2 ==0:
#         print(i)


# #loops on index:
# l = [10,20,30,40,50,99,189,7,56]
# for i in range(len(l)):
#     print(f'{i} => {l[i]}')



# l=[12,3,5,6,7,433,3,233,45,7,54,34]

# for i in range(len(l)):
#     print (f"{i} =>{l[i]} ")



#list methods
# l = [45,12,89,23,67,23]
# l.append(40)
# print(l)

# l = [45,12,89,23,67,23]
# l.clear()
# print(l)

# a = [45,12,89,23,67,23]
# b =a

# b[0]=100
# print(a)


# a = [45,12,89,23,67,23]
# b =a.copy()
# b[0]=100
# print(a)
# print(b)

# a = [1,2,3,1,1,1,4,3,54]
# print(a.count(1))
# print(a.extend([10,20,30]))
# print(a.index(3))
# a.insert(0,"hello")
# print(a)


# a = [10,30,20]
# popped = a.pop(1)
# print(a)
# print(popped)
# a.remove(10)
# print(a)

# a.reverse()
# print(a)


# a = [10,30,20]
# a.sort(reverse=True)
# print(a)


# a = [10,20,30,40,50]
# b=[]

# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)


# a =[10,20,30,40,50,60,70,80,90,100]

# temp = len(a)-1
# for i in range(0,(len(a))//2):
#     a[i],a[temp] = a[temp],a[i]
#     temp = temp -1

# print(a)




# prectic classess
# print list element in Reverse Order
# (inter change element )
# arr = [12,32,4,45,3]

# n = len(arr)
# for i in range(0,n//2):
#     arr[i],arr[n-i-1] = arr[n-i-1], arr[i]
# print(arr)

# Q2. print positive and negative element of a list 
# print positive and negative element separately ignore Zero
# arr =[12,4,-5,2,-34,-23]

# print("positive:",end ="")
# for i in arr:
#     if i>0:
#         print(f"{i}",end="")
# print("Negastive :",end ="")
# for i in arr:
#     if i<0:
#         print(f"{i}",end="")
# list = [10,20,30,40]
# sum = 0
# for element in list:
#     sum += element

# print(f"mean -->{sum//len(list)}")
# Q4. find the greatest element and its index
# find the grestest element and print its index
# Example:
# input = [2,96,69,77,145,20]
# output =: max element = 145 found t 4 index
# arr = [2,96,69,77,145,20]

# max = arr[0]
# index =0
# for i in range(1,len(arr)):
#     elem = arr[i]
#     if elem > max:
#         max = elem
#         index =i

# print(f"max is {max} at index {index}")


# find trhe missing number 
# .A list contains numbers from 1 to N , but one number
# is missing .write a program to find the missing number
# EX:==
# a=[1,2,4,5]
# output :=
# missing number = 3

# arr = [1,2,4,5]
# n = len(arr)
# og_n =n+1
# og_sum =0
# for i in range(1,og_n+1):
#     og_sum +=i
# real_sum =0
# for elem in arr:
#     real_sum += elem
# missing = og_sum - real_sum
# print(missing)
# check whether a List is sorted or not 

# check if the list element are 
# arranged in ascending order

# EX:==
# input=== [10,20,30,40,50]
# output == List is sorted 
# arr = [10,20,30,40,50]

# n = len(arr)

# is_sorted = True

# for i in range(0,n-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("list is sorted")

# else:
#     print("List is not sorted")



# PALINDROMIC lIST

# check the same the list
# reads the sume from and back.

# Example:==
# input = [2,3,15,3,2]
# output = palindromic List
# arr =[2,3,15,3,2]
# n = len(arr)

# is_palindrome = True

# for i in range(n//2):
#     if arr[i] !=arr[n-i-1]:
#         is_palindrome = False

# if is_palindrome:
#     print("palindrome")

# else:
#     print("not a palindrome")
# n = int(input("Enter how many elements: "))

# arr = []

# for i in range(n):
#     num = int(input("Enter number: "))
#     arr.append(num)

# print("Array:", arr)
# Q.sort a List in ascending order
# babal sort
# write 
# arr = [64,34,25,12,22,11,9]
# n  = len(arr)

# for i in range(n):
#     for j in range(n-1-i):
       
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

# print(arr)
# selection sort
# arr = [64,34,25,12,22,11,9]



########################################################################
###########################DICTIONARY##############################
#--------------------------------------------------------------------

# Dictionary:::===
# 1.""""""
# 2.  Annoted by {curly brackets}
# 3.  Dictionary is combinations multiple leys:values
# 4 ''''''
# 6.d = {}  Empty Dictonary

# 3. Dictionary are mutable.
# 4. dictionary are hectrogenous
# 5. Ductionary are ordered
# 6.values can be dublict but keys can  not dublict  (In dict keys will always be UNIQUE but values )
# 7.

# d = {1:10,2:20,3:30,4:40}
# d[3]= 100
# print(d)
# d = {1:10,2:20,3:30,4:40,2:200} # 
# print(d)
# d = {1:10,2:20,3:30,4:40} # 5:50
# d[5]= 50# creating new key and assigning value.
# print(d)
# # agar hum direct loop run karte hai dictionary pe toh we will gwt KEYS
# d = {1:10,2:20,3:30,4:40}
# for i in d:
#     print(i,d[i])
# #method in Dictionaryu
# #1. .keys()
# #to print or give only and only KEYS from the DICT.
# 2. .values()
# will give all the values from the dictionary
# 3. .items()
# d = {"a":1.0,"b":2.0,"c":3.0,}
# print(d.keys())
# print(d.values())
# #items
# print(d.items())
# d = {"a":1.0,"b":2.0,"c":3.0,}
# for key, value in d.items():
#     print(key,value)
# d = {"a":1.0,"b":2.0,"c":3.0,}
# d.pop("c")
# print(d)


#============================ONLINE CLASS ========================================

# find the pair with the given sum
# find all pairs of elements whose sum quuals a given target
# Example:
# input :[2,4,3,5,7,8]
# target :10
# output:
# (2,8)
# (3,7)
# n = [2,4,3,5,7,8,]
# target = 10
# arr = len(n)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i],arr[j])

# Question : check whether a List is a sublist of another List
# write a python prigtam to check whether all element of one list appear consecutively in another list,

# Example:
# input:
# arr= [10,20,30,40,50]
# sub = [20,30,40]
# output:
# sublist found
# #itself
# arr= [10,20,30,40,50]
# sub = [20,30,40]
# found = False
# for i in range (len(arr)):
#     if arr[i:i+len(sub)] == sub :
#         found = True
#         break

# if found:
#     print("Sublist Found")

# else:
#     print("Not Found")
# arr= [10,20,30,40,50]
# mn = len(arr)
# sub = [20,30,40]
# m = len(sub)

# for i in range(0,n-m+1):
#     if arr[i:i+m] == sub:
#         print("SUBLIST FOUND")
#         break
# else:
#     print("NOT FOUND")


# Question: Rotate a List to the Right by K Positions
# Write a Python program to rotate a list to the right by K positions
# using a loop.
# Example:
# Input:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Output:
# [4, 5, 1, 2, 3]
# arr = [1, 2, 3, 4, 5]
# k = 2



# Question: Sort a List in Ascending Order
# Write a Python program to sort the elements of a list in
# ascending order without using the built-in sort() method.
# Example:
# Input:  [64, 34, 25, 12, 22, 11, 9]
# Output: [9, 11, 12, 22, 25, 34, 64]
# arr = [64,34,25,12,22,11,9]
# n  = len(arr)

# for i in range(n):
#     for j in range(n-1-i):
       
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

# print(arr)
# arr = [64,34,25,12,22,11,9]
# n  = len(arr)

# for i in range(n):
#     for j in range(n-1-i):
        
#         if arr[j] > arr[j+1]:
#              arr[j],arr[j+1]= arr[j+1],arr[j]
# print(arr)





####################################################################
#===================SETS=========================================
#########################################################################


# 1.sets
# 2.sets are annoted by {} or set()
# 3.Empty {}-> dict but {1,2,3,4,} -> set.
# 4. Empty {} -> dict but {1,2,3,4} ->set.
# 5. sets are hetrogenous
# 6. sets are Unordered.
# 7. as sets don't have indexing we cannot replace anyvalue.
# 8. No dublicate 

# s  ={1,2,3,4}
# print(type(s))
# s1 = {1,2,3,4,True,80.2,"sample"}
# print(s1)

# l  =[1,1,2,3,4,4,5]
# print(set(l))

# #METHOD OF SET
# s = {1,1,2,3}
# s.add(4) .add ()-> to add any element from set.
# s.remove(3)
# print(s)
# #.discard ()-> if element is not present inside od set so it will not reise any error.
# s.remove(3)
# print(s)
# s = {1,1,2,3}
# s.add(4)
# print(s)

# s.remove(3)
# print(s)

# SET OPERATIONS...
# 1.UNION -> merge both the sets.
# 2.INTERSECTION -> Common element
# 3.Difference -> ese elements jo ek set but dusre mai nahi.
# 4.SYMMETRIC DIFFERENCE -> common element ko remove karke sata hai 
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(f"union:={s1.union(s2)}")
# print(f" intersection:={s1.intersection(s2)}")
# print(f"difference:={s1.difference(s2)}")
# print(f"difference:={s2.difference(s1)}")
# print(f"symmetric_difference:={s1.symmetric_difference(s2)}")

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(f"Union -> {s1 | s2}")
# print(f"UINTERSECTION -> { s1 & s2}") #& and 
# print(f"difference:={s2- s2}")
# print(f"symmetric_difference:={s1 ^ s2}")
# s = frozenset([1,2,3,4,5])
# s.add(6)
# s.remove(1)

# print(s)



###############################################################################
#==================TUPLES=====================================================
###############################################################################


# 1. tuple..
# 2. A tuple is an ordered , immutable collection.
# 3. once you create it, you can't change , add or remove items

# 1.Annoted by (paranthesis).
# 2. ordervalues -> their are indexing
# 3. Hetrogenous -> Mixed types values are allowed
# 4.Immutable
# 5. 
# t =()
# print(type(t))
# t =(1,2,3,4)
# print(t[3])
# t =(1,2,3,4,5,6,7,8)
# print(t[1:5])
# print(t[::-1])
# METHOD 
# 1#. count() -> count the occurence of amy value

# #2.. INdex () -> Shpw the index location of the first occuring element.
# t = (1,2,1,2,1)
# print(t.count(1))
# print(t.index(2))
# + -> two tuples can concatatenate
# * -> repetiting
# t1 = (1,2)
# t2 = (3,4)
# print(t1 + t2)
# print(t1 * 5)

# t = (1,2,[2,3,4])

# t[2].append(100)
# print(t)