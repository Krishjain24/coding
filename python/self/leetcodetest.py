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
