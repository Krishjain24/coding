#sum of digits of a number 
"""# 123 1+2+3=6
n=int(input("enter number:")) #123
#while <condition >: for ex  while is used when we know ki kis condition
# tak loop run karana hai 
sum=0
while n!=0:
    # maths n/10 ex 123/10 =12.3
    # 123//10=12  (floor division - it removes the decimal part )
    # 123%10= 3
    sum+=n%10 #sum=sum+ n%10
    n=n//10  # to reduce the last value 
print(sum)"""
    
##use of try and except
"""try:
    n=int(input("enter number:"))
    for i in n:
        print(n%10)
except TypeError :
    print("this code doesnt work ")"""
    
## sum of digits of given number using for loop 
"""n=(input("enter your value:"))
s=0 #sum
for i in n:
    s+=int(i)
print(s)
"""
## if said that input is  in for m of integer 
"""n=int(input("enter your value:"))
s=0
for i in str(n):
    s+=int(i)
print(s)"""

##ATM pin verification system using while loop with errorhandling
"""print("welcome to krish jain ATM:-\n enter your pin\n remember you have only 3 tries and\n if you tried any cheating then your tries ends intantly ")
tries=3
try:
    while tries>0:
        n=(input("Pin:"))
        if len(n)==4 and n==1234: 
            print("Access granted\nwelcome to your account")
            break
        elif len(n)==4 and n!=1234:
            tries=tries-1
            if tries>0: 
                print(f"incorrect pin\nyou have only {tries} Tries left")
            elif tries==0:
                print("card blocked\n contact to your bank")
        else:
            print("pin is in between 0000 and 9999")
except ValueError:
    print("are you idiot!!! enter a valid entry")"""

# nums = [1,2,3,1,1,3]
# count=0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         if nums[i]==nums[j] and i<j:
#             count+=1
# print(count)
""" count=0
nums = [4,3,2,1]
for i in range(len(nums)):
    if i%10==nums[i]:
        count=i
        break
print(count)
 """

import pandas as pd

# 1. Dictionary: create, access, add, update, and remove items
print("=== Dictionary ===")

student = {
    "name": "Anaya",
    "age": 20,
    "course": "DSA"
}

print("Original dictionary:", student)
print("Student name:", student["name"])

student["grade"] = "A"                 # Add an item
student["age"] = 21                    # Update an item
student.pop("course")                  # Remove an item

print("Modified dictionary:", student)


# 2. Tuple: create, access, count, and find an item
print("\n=== Tuple ===")

subjects = ("Python", "C++", "Java", "Python")

print("Tuple:", subjects)
print("First subject:", subjects[0])
print("Number of times Python appears:", subjects.count("Python"))
print("Index of Java:", subjects.index("Java"))

# Tuples are immutable, so they cannot be changed directly.
# To change one, convert it to a list and then back to a tuple.
subject_list = list(subjects)
subject_list.append("DSA")
subjects = tuple(subject_list)

print("Tuple after adding DSA:", subjects)


# 3. Set: create, add, remove, and perform set operations
print("\n=== Set ===")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

set_a.add(7)                   # Add an item
set_a.discard(1)                # Remove an item

print("Set A after modification:", set_a)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)


# 4. DataFrame: create, add a column, update, filter, and drop a column
print("\n=== DataFrame ===")

df = pd.DataFrame({
    "Name": ["Anaya", "Rohan", "Meera"],
    "Age": [20, 19, 21],
    "Marks": [85, 92, 76]
})

print("Original DataFrame:")
print(df)

# Add a column
df["Result"] = ["Pass" if mark >= 40 else "Fail" for mark in df["Marks"]]

# Update a value
df.loc[0, "Marks"] = 88

print("\nDataFrame after adding Result and updating marks:")
print(df)

# Filter rows where marks are at least 80
high_scorers = df[df["Marks"] >= 80]
print("\nStudents with marks of 80 or more:")
print(high_scorers)

# Drop a column
df = df.drop(columns=["Age"])
print("\nDataFrame after dropping the Age column:")
print(df)


