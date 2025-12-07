def find_consecutive(nums):
    counter = 0
    biggest = 0

    for i in nums:
        if i == 1:
            counter +=1
                
        else:
            if counter > biggest:
                biggest = counter
            counter = 0
    if counter > biggest:
        biggest = counter
    
    
    return biggest
        
list = [1,0,1,1,0,1]
print(find_consecutive(list))