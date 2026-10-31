## data structures ->used for storing multiple values eg- marksa of 70 marks
#they are of 4 types  list ,tuple ,set ,dictionary
#1.()-> tuples
#2.[]-> list
#3.{}-> set ,dictionary

##1.List
a=[]
print(type(a))   #<class 'list'>
#heterogeneous nature-> you can store multiple data types
"""a=["harsh",28,True,12.2,print()]"""
#INDEXING-> same as string
#mutable nature ->you can change the value of your list
"""l=[10,20,30,40,50]
print(l[1:4])"""  #[20, 30, 40]

"""l[0]=100000
print(l)""" #[100000, 20, 30, 40, 50]                                     

##loops on list:
"""l=[10,20,31,41,50]"""
#1. loop on values
"""for i in l:
    if i%2==0:
        print(i)"""

#2.loop on index:
"""for i in range(len(l)):
    print(i)
    print(f"{i}->{l[i]}")"""
  