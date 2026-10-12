##continue

for i in range(1,21):
    if i%2==0:
        continue
    print(i)

##prime number another approach by using break and else
"""n=int(input("enter no:"))
for i in range(2,n):
    if n%i==0:
        print("composite")
        break  
else:
    print("prime")"""

##check if a number is prime or not using break and else approach and also using half range 
"""n=int(input("enter no:"))
for i in range(2,n//2+1):  #“The greatest proper factor of a positive integer is at most half of the number.”
    if n%i==0:
        print("composite")
        break  
else:
    print("prime")"""

##print the prime numbres 
"""n=int(input("tell your range:")) 
for j in range(2,n+1):
    for i in range(2,(j//2)+1):
        if j%i==0:
            break
    else:
        print(j)"""

##hw-find the highest common factor 