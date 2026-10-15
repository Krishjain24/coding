""" dictionary 
1. annotated by {curly braces}
2.dictionary id a combination of multiple keys:values
3. dictionaries are mutable 
4.dictionaries are heterogeneous
5.dict are ordered
6. in dict key will always be UNIQUE but value can be duplicate"""
"""# d={} #empty string 
d={1:10,2:20,3:30}
# print(d[1])
# d[3]=100
# print(d)

d[5]=50 # creating and assigning new values
print(d)
"""
#agar hum direct loop run karte hai dict pe to we will get keys 
"""d={1:10,2:20,3:30}
for i in d:
    print(i,d[i])"""

#methods in dictionaries
#1..keys():-> to print or give only KEYS from the dictionaries
# to print single key we need loop with if condition
"""d={"a":1.0,"b":2.0,"c":3.0}
print(d.keys())"""

#2..values():-> will give all the values from the dictionaries
"""d={"a":1.0,"b":2.0,"c":3.0}
print(d.values())"""

#3. .items():-> to gety both keys and values from the dictionaries
"""d={"a":1.0,"b":2.0,"c":3.0}
print(d.items())"""

## to print key and value in a single loop 
"""d={"a":1.0,"b":2.0,"c":3.0}
for key,value in d.items():
    print(key,value)
"""

#4. .pop(key):-> remove the  key and value from the dictionaries
d={"a":1.0,"b":2.0,"c":3.0}
d.pop("b")
print(d)
