def missingNumber(nums):
    mySet = set(nums)

    for i in range(len(nums)+1):
        if i not in mySet:
            return i



print(missingNumber([3,0,1]))