#brute force
def sortArrayByParity(nums:list[int]):
    odd = 1
    even = 0

    while even < len(nums) and odd < len(nums):

        
        if nums[even] % 2 == 0:
            even += 2

        if nums[odd] % 2 != 0:
            odd += 2

        else:
            tmp = nums[even]
            nums[even] = nums[odd]
            nums[odd] = tmp
    return nums 


                



print(sortArrayByParity([4,2,5,7]))