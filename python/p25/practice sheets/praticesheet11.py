##DATE:->24/09/26
#Q1.
even,odd=0,0
n=int(input("enter your range of numbers:->"))
for i in range(n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
if even>odd:
    print(f"the diff between the sum of even and odd is{even-odd}")
else:
    print(f"the diff between the sum of even and odd is{odd- even}")

    
