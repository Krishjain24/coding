##DATE:13/09/26
##Q1.Write a Python program to print the first character of the given string.  
"""word = input("Enter a word: ")
if len(word) > 0 and word.isalpha():
        print(f"The first character of the given string is: {word[0]}")
else:
        print("Please enter a valid alphabetic string.")
"""
##Q2.Write a Python program to print the last three characters of the given string.
"""a=input("enter a string :")
if len(a)>0 and a.isalpha():
    print(f"the last three letters is:-{a[-3::1]}")
else:
    print("use a valid string!") """ 

##Q3.Write a python program to reverse the given string using slicing"
"""a=input("enter a string :")
if len(a)>0 and a.isalpha():
    print(f"The Reverse order of the string is:-{a[::-1]}")
else:
    print("use a valid string!")"""

##Q4.write a python program to print every second character of the string
"""a=input("enter a string :")
if len(a)>0 and a.isalpha():
    print(f"the every second of the string is:-{a[::2]}")
else:
    print("use a valid string!")"""

##Q5.the numbers are given as strings.convert them into integers and print their sum
"""a="25"
b="15"
print(f"The sum of a and b is: {int(a)+int(b)}")"""

##Q6.The numbers are given as strings.convert them into strings and find their remainder
"""a="27"
b="5"
print(f"The remainder of a and b is:{int(a)%int(b)}")"""

##Q7.Take a number as an input and print the cube of it 
"""a=float(input("enter the number:"))
print(f"the cube of the given number is: {a**3}")"""

##Q8.Take three numbers as input and print their total and average
"""a=float(input("enter three numbers:"))
b=float(input())
c=float(input())
sum= a+b+c
average=sum/3
print(f"The sum of all three values is {sum} and their average is{average}")"""

##Q9.take the price and discount percentage as input .calculate the discount amount and final price.
"""a=float(input("enter the amount:"))
b=float(input("enter the discount percentage:-"))
discount_Amount=b/100*a
final_price=a-discount_Amount
print(f"The discount amoouont is{discount_Amount} and final price is {final_price}")"""

##Q10.Take the tempreature in celcius as input and convert it into fahrenheit.
"""a=float(input("Tell the Temperature(in Celsius):-"))
print(f"The current Temperature in Farenheit is:-{(a*(9/5))+32} ")"""