nums = [5,5]

def getSum(target,nums):
    x = nums[0]
    j = target - x

    size = len(nums)
    for i in range(1,size):
        
        if nums[i] == j:
            return [nums.index(x) , i] 

print(getSum(10,nums))