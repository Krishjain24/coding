##OOPS             
#Date=16/11/2026
##CLASS

##1. how to create a class:->
""" class <classname>: """
class College:
    ...

##Attributes and methods 
""" A variable defined inside a class is called attribute 
A function defined inside a class is called method """
# ex
""" class Animal:
    name ="lion" # attributes 
    print("how are you")
    for i in range(12):
        print("hell")
    def speak(): # method
        print("lion roars")
 """
## everything inside a class is initialized only a single time
##so that means  everyline inside the class is going to get executed  once

#2. accessing attributes and methods 
""" class students:
    name ="harsh"
    def details():
        print("hello his name is harsh")

print(name) # it is an attribute thats why it cant access
print(students.name) ## method to access attribute 
students.details() """ ##  to access methods

### OBJECTS 
""" if we call a class inside a variable, that variable become an object
ex:->"""
class Animal:
    name="harsh"

obj = Animal() #here we created an object
print(obj.name) ##

# -------------------------------------------------------------------------------------------------------------------------------
# date=17/11/26

""" object can also acccess the attributes and methods define inside a class """
""" when you call any method using an object ,your object location is passed """
class Factory:
    name= "puma"
    def details(self):
        print("hello this is the puma factory")

a=Factory()
print(a.name)
a.details()  # TypeError: Factory.details() takes 0 positional arguments but 1 was given ( this error comes when you dont use any parameter in method) 

##constructor  function 
""" a constructor functions is a type of dunder method that will be automatically called once you create an object and it will alsi capture the location of your object in self """
class Registration:
    def __init__(self):
        print(self)
        print("how are you ")
    print("hello")

a=Registration()
b=Registration()
c=Registration()

# output
""" hello
<__main__.Registration object at 0x0000020C7CC88C20>
how are you 
<__main__.Registration object at 0x0000020C7CC68410>
how are you 
<__main__.Registration object at 0x0000020C7CC68690>
how are you  """

class Registration:
    def __init__(self,name,age,no,gender):
        self.name= name
        self.age=age
        self.no=no
        self.gender=gender
    print ("hello")

a=Registration("harsh",22,1234567,"M")










































