def runningSum(nums):
    l=[nums[0]]
    print(nums)
    for i,b in enumerate(nums):
        print(i)
        if i>0:
            if i > len(nums)-1:
                pass
            else:
                l.append(nums[i] + l[i-1])
        else:
            pass
    print(l)

bill=[1,1,1,1,1]
kill=[1,2,3,4]
runningSum(bill)