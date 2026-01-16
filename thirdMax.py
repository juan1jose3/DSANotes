def thirdMax(nums:list[int]):
    numbers = set(nums)
    if len(numbers) > 2:
        
        biggest = 0
        for _ in range(3):
            biggest = max(numbers)
            numbers.remove(biggest)

    
        return biggest
    else:
        return max(numbers)
    

    




print(thirdMax([1,1,2]))