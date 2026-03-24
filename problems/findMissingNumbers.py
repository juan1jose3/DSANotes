def findMissing(nums): 
    missing = []
    seen = (nums)
    
    for i in range(1,len(nums) + 1):
        if i not in seen:
            missing.append(i)
    return missing
    
   




list = [4,3,2,7,8,2,3,1]
print(findMissing(list))