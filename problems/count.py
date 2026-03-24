nums = [1,2,3,3]

def getRepeated(nums):
    for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    counter +=1
                if counter > 1:
                    return True
    return False

print(getRepeated(nums))