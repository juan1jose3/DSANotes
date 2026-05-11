def search(nums: list[int], target):
    start = 0
    end = len(nums) - 1
    size = len(nums) - 1

    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1

    while end >= start:
        middle = end + start // 2
        
        if middle > size:
            return -1

        if nums[middle] == target:
            return middle
        
        elif nums[middle] < target:
            start += 1

        else:
            end -= 1
        
        
    return -1


print(search([-1,0,3,5,9,12], 13))