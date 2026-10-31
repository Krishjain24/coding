for i in range(n):
    nums1.pop(-1)
for i in range(n):
    nums1.append(nums2[i])
nums1.sort()
print(nums1)