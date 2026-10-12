#11\9\2026
#type conversion 
#int() ,float(), str(),bool()
"""when you want to convert one data type to another data  type you have to use type conversion
int float and str are basic but if we talk about bool there are some falsy values 
(0,0.0,"",{},[],(),None,false)"""


##input and output
"""for providing the output you have only one thing and that is print()"""
#how you can use variable while printing 
"""name = "yash"
age = 20 
#first way 
print("hello how are you",name,"and your age is", age)

#second way 
print(f"hello how are you {name} and your age is {age}") # this is known as formatted string """


#input 
"""input are simple but make sure to have the right data types while taking the inputs """

name=input("tell your name:")
age = int(input("tell your age:"))
temp=float(input("tell the temperature:"))
print(name,age,temp)