##comparison operator
#(==,>,<,>=,<=,!=)
"""a=10
b=20"""
"""print(a==b) #left side and right side must be equal 
print(12.5>12) #it can compare between two datatypes 
print("ABC"< "ABD") # it compare ASCII value of strings word by word 

print(13.4>78) #false(float and int can be compared)
print(bool("")==False) #true (coz type conversion make them same datatype )
print("H">34) # error ( coz it convert string to ascii value) """

## logical operator 
""" when you have to get a single result out of multiple comparisons you have to use logical operator 
(and ,or not )
# 1.AND= AND operator says all the comparison must be  true
print(12!=12 and 12<13) # false
# 2.OR= OR says out of all the comparison any one can be true 
print(12!=12 or 12<13) #true
# 3. NOT= NOT operator converts true to false and false to true 
# print(not 12==12) # false """

#que
"""print((12==45 or 23== 45 or not 12!=12)and(bool(34) and 34==34))""" #true