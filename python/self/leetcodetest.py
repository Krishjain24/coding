def sumOfSquares(nums: List[int]) -> int:
    l=len(nums)
    sum=0
    for i in range(l):
        a=nums[i]
        if a%l==0:
            sum=sum+a*a
        return sum