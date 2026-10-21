##tuple
""" a tuple is an ordered,immuatable collection,once you create it you cant change ,add or remove items
1. annonated by (parenthesis) 
2.tuple are ordered-there are indexes 
3. heterogeneous -mixed type values are allowed 
4.duplicate elelment are allowed
5. immuatable 
6. slicing - same as string and list"""


t=()    ##empty tuple
"""print(type(t))      # to print the type of data structure
t=(1,2,3,4,"hello",32.7,True)"""

## reverse the tuple using slicing 
"""t=(1,2,3,4,"hello",32.7,True)
print(t[::-1])
"""

## methods 
#1. .count()-> count the occourence of any value
#2. .index()-> show the index location of the first occuring element 

"""t=(1,,2,1,2,1,2)
print(t.count(1))
print(t.index(2))"""

""" 
OPERATIOIN
+ -> two tuple are concateate
"""
"""t1= (1,2)
t2= (3,4)
print(t1 + t2)
print(t1*5)
"""

t=(1,2,[1,2,3])
t[2].append(100)
print(t[2])

