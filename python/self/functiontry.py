""" def addition (a,b):
    print("how")
    12+22
    print("a+1",a+b)
addition(b="True",a="23") """
""" 
def IsPalindrome(n):
    sum=0
    temp=n
    while n!=0:
        sum=sum*10+n%10
        n//=10
    if sum==temp:
        return True
    else:
        return False
print(IsPalindrome(121))
 """
""" 
def create_profile(username, **kwargs):
    print(f"User: {username}")
    # kwargs behaves just like a normal dictionary
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

create_profile("alex_dev", age=28, city="Bhopal", role="Engineer") """
""" count=0
nums = [0,1,0,3,12]
while 0 in nums:
    nums.remove(0)
    count+=1
for i in range(count):
    nums.append(0)
print(nums) """
""" count=0
arr1 = [4,5,8]
arr2 = [10,9,1,8] 
d = 2
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if  (arr1[i]<arr2[j]) and ((arr1[i])-(arr2[j])<d or  (arr2[j])-(arr1[i])<d):
            continue
    else:
        count+=1
print(count) """
""" large=0 #3
large2=0 #0
large3=0 #0
nums = [3,2,1]
for i in range(len(nums)):
    if nums[i]>large:
        large3=large2
        large2=large
        large=nums[i]
    elif nums[i]>large2:
        large3=large2
        large2=nums[i]
    elif nums[i]> large3:
        large3=nums[i] """
# print(large,large2,large3)

nums =[-1,-2,-3,3,2]
nums.sort()
print(nums)
nums=set(nums)
print(nums)
nums=list(nums)
print(nums)
# if len(nums)>=3:
#     print (nums[-3])
# else:
#     print (nums[-1])
# print(len(nums))
for i in range(1,234):
    ...