def singleNumber(nums):

    init = 0
    for num in nums:
        init = init ^ num
    return init



    """
    count = {}
    counter = 1

    for num in nums:
        if num not in count:
            count[num] = counter
        else:
            count[num] += counter
    print(count)
    
    for num in count:
        if count[num] == 1:
            return num
    """





print(singleNumber([4,1,2,1,2]))