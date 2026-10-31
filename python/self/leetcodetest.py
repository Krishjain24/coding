""" def sumOfSquares(nums: List[int]) -> int:
    l=len(nums)
    sum=0
    for i in range(l):
        a=nums[i]
        if a%l==0:
            sum=sum+a*a
        return sum """
""" 
nums = [1,2,5,2,2,3]
nums.sort()
ans=[]
target=2
for i in range(len(nums)):
    if nums[i]==target:
        ans.append(i)
print(ans) """


""" s = "(()"
garb=0
ans=0
index=0
for i in enumerate(s):
    if (c=="(" and(c=="(" and i==index+1)):
        garb+=1
    if (c==")" and(c==")" and i==index+1)):
        garb+=1
    if  (c==")" and(c=="(" and i==index+1)):
        garb+=1
    else:
        ans+=2
print(ans) """
# def function(s):
"""     index=0
    for i,c in enumerate(s):
        if (i== index and c=="("):
            index+=1
            if (i==i+1 and c==")"):
                return True
        else:
            return False
print(function("()"))
 """
""" 
nums1 = [1,2,3,0,0,0]

for i in range(3):
    nums1.pop(-1)
print(nums1) """
""" 
nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

for i in range(n):
    nums1.pop(-1)
for i in range(n):
    nums1.append(nums2[i])
nums1.sort()
print(nums1)

 """

""" s="1234"
if s.isdecimal() or s.isdigit() or s.isnumeric():
    print(True)
else:
    print(False) """

def check(s:str) -> bool:
    if not s.isalpha() :
        if s.isdecimal() or s.isdigit() or s.isnumeric():
            return True
        if "."in s:
            s.split()
            for i in s:
                if s in "1234567890" and s in ".":
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
print(check(".1"))
