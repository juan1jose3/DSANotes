def removeElement(nums:list[int], val:int):

    i = len(nums) - 1

    while i >= 0:
        if nums[i] == val:
            nums.remove(nums[i])
        i-=1
    return len(nums)


       



print(removeElement([1],1))
