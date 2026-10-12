 #10\9\2026
##string
"""every thing inside a string is unicode(just like ASCII valueof cpp) and to find you have to use ord() function 
chr() function- used to convert unicode value into character"""
#name= "A"
#print(ord("A"))
name= "Ashish" 
print(ord(name[0])) #use ord() function to find out the unicode value of first character of string. the output will be 65 and the value of A in string is 0 it is identified by index value 0 and the value of s is 1 and so on
 
##indexing
"""every element inside your string can be accessed using index
there are two types of indexing one is positive starting from 0 and one is negative, starting from -1"""
#s="robot 922"
#print(s[-5],s[4]) #output  t t 

 ##slicing
"""whenever you want to extract a portion of your string you can use slicing.
there are three points in slicing [start ,stop ,steps]
and three point take index value of  your string"""
"""a= "ROBOT 922"
print(a[0:5:1]) # output is ROBOT
print(a[6:9:1]) #output is 922"""

##Default value of slicing 
"""[0:last value:1]"""





