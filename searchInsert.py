def searchInsert(nums:list[int] , target:int):
    
    """
        for i in range(0,len(nums)):
            
            if nums[i] == target:
                return i
        nums.append(target)
        nums.sort()
        
        for j in range(0,len(nums)):
            if nums[j] == target:
                return j


    we use instead binary search
    During binary search:

    If the target is less than nums[mid], you move the end left.

    If the target is greater, you move the start right.

    Eventually:

    start moves forward until it lands exactly where the target should go.
    
    """


    start = 0
    end = len(nums) -1

    while end >= start:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


    
    
    
  
      




print(searchInsert([1,3,5,6],2))