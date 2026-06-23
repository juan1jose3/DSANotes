def majorityElement(nums):
    n = len(nums)
    equation = n // 2
  


    counter = 1
    candidate = nums[0]
    current = 0

    for current in nums:
        if counter == 0 and candidate != current:
            candidate = current

        if current == candidate:
            counter += 1
        else:
            counter -= 1

    
    if counter == 0 and candidate != current:
            candidate = current
    return candidate
        




        
    



print(majorityElement([6,5,5]))