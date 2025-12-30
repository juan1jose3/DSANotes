def removeSorted(nums:list[int]):
    w = 0
    for r in range(1,len(nums)):
        if nums[r] != nums[w]:
            w += 1
            nums[w] = nums[r]
        

        
    return w + 1


   
        





print(removeSorted([1, 1, 2, 2, 3]))