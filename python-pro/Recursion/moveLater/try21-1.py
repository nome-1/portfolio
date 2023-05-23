nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
n=len(nums2)
idx = 0
for i in range(len(nums1)):
    if idx >= n:
        break
    if nums1[i] == 0:
        nums1[i] =nums2[idx]
        idx += 1
nums1.sort()
print(nums1)
