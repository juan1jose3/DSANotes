def find_missmatch(nums): 
    for i in nums:
        home_index = abs(i) -1
        
        if nums[home_index] < 0:
            continue
        else:
            nums[home_index] = nums[home_index] * -1 # we store the modified value on the array
        
    print(nums)

    missing = []
    for j in range(len(nums)):
        if nums[j] > 0:
            missing.append(j+1)
    
    return missing
        



list = [4,3,2,7,8,2,3,1]

print(find_missmatch(list))



'''
Better code 

seen = set(nums)

missing =[]
for i in range(1,len(nums)+1):
    if i not in seen:
        missing.append(i)
return missing

'''