def removeElement(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums,val))


def removeElemen1(nums, val):
    box = []
    for i, t in enumerate(nums):
        if t != val:
            box.append(t)
    k = (box)
    return k