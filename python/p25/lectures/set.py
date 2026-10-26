""" SETS
1.sets
2.sets are annoted by {} or set()
3.Empty {}-> dict but {1,2,3,4,} -> set.
4. Empty {} -> dict but {1,2,3,4} ->set.
5. sets are hetrogenous
6. sets are Unordered.
7. as sets don't have indexing we cannot replace anyvalue.
8. No dublicate 
"""
"""s  ={1,2,3,4}
print(type(s))
s1 = {1,2,3,4,True,80.2,"sample"}
print(s1)"""

"""
l  =[1,1,2,3,4,4,5]
print(set(l)"""

## METHOD OF SET
#1. .add(element) -> to add any element from set.
"""s = {1,1,2,3}
s.add(4) 
print(s)"""

#2. .remove(element)-> to remove any value from set
"""s = {1,1,2,3} 
s.remove(3)
print(s)"""

#3. .discard (element)-> if element is not present inside of set so it will not raise any error. 
"""s = {1,1,2,3}
s.discard(1)
print(s)"""

## difference between  remove and discard:-
""" remove() is strict- means if we remove a value which is not in set,it gives  Typeerror
whereas discard() is safe -It changes nothing and exits quietly if the item is missing.
"""



## SET OPERATIONS...
"""1.UNION -> merge both the sets.
2.INTERSECTION -> Common element
3.Difference -> ese elements jo ek set but dusre mai nahi.
4.SYMMETRIC DIFFERENCE -> common element ko remove karke sata hai """

"""s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(f"union:={s1.union(s2)}")
print(f" intersection:={s1.intersection(s2)}")
print(f"difference:={s1.difference(s2)}")
print(f"difference:={s2.difference(s1)}")
print(f"symmetric_difference:={s1.symmetric_difference(s2)}")
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(f"Union -> {s1 | s2}")              # | -> can be used as union 
print(f"UINTERSECTION -> { s1 & s2}")     # & -> can be used as intersection 
print(f"difference:={s1- s2}")            # - -> can be used as  difference
print(f"symmetric_difference:={s1 ^ s2}") # ^ -> can be used as symmectric difference

##frozenset 
"""
A frozenset is an immutable (unchangeable) version of a Python set. Once created, elements cannot be added, removed, or modified. Just like regular sets, they are unordered and automatically eliminate duplicate values.

## Key Characteristics
1.Immutable:->Methods like `.add()`, `.remove()`, or `.discard()` do not exist and will raise an `AttributeError`.
2.Hashable:-> Because they cannot change, `frozenset` objects can be used as **dictionary keys** or as **elements inside other sets** (which normal sets cannot do).

## Syntax & Quick Example
```python
# Creation from an iterable (list, tuple, set)
numbers = frozenset([1, 2, 2, 3])
print(numbers)  # Output: frozenset({1, 2, 3})

# Attempting to modify raises an error
# numbers.add(4) -> AttributeError
```

## Allowed Operations
You can still perform standard mathematical operations that return a **new** set object:
* `set1.union(set2)`
* `set1.intersection(set2)`
* `set1.difference(set2)`"""
""" 
s = frozenset([1,2,3,4,5])                #
s.add(6)
s.remove(1)

print(s) """


s={"y"}
for i in s:
    print(i)