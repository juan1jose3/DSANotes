def majorityElement(nums):
    n = len(nums)
    equation = n // 2
  


    counter = 0
    candidate = nums[0]
    current = 0

    for current in nums:

        if current == candidate:
            counter += 1
        else:
            counter -= 1
        
        if counter <= 0 and candidate != current:
            candidate = current
            counter = 1



    return candidate
        




        
    



print(majorityElement([1,3,1,1,4,1,1,5,1,1,6,2,2]))