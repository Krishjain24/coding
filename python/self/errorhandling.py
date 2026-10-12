num = input("Enter a valid number: ")
"""try:"""
num = int(num)
print(num)
"""except ValueError:
    print("enter a valid number")"""


# numa = 100
# numb = 00

# def divi(a, b):
#     return a / b

# try:
#    reslut = divi(numa, numb)
#    print(reslut)
# except ZeroDivisionError:
#     print("Cant divide by zero")
    
if num==1:    
    raise ValueError("Ye number nahi chalega error")