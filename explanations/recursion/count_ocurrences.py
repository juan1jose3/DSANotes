def count_ocurrences(list, target):
    counter = 0
    if len(list) == 0:
        return counter

    if list[0] == target:
        counter += 1
     
    return counter + count_ocurrences(list[1:], target)



print(count_ocurrences([3, 5, 3, 3, 7], 3))