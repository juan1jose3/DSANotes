def binary_search(list , target, start, end):

    if start > end:
        return False 

    middle = start + (end - start) // 2

    if list[middle] == target:
        return middle
    
    elif list[middle] > target:
        end = middle - 1

    elif list[middle] < target:
        start = middle + 1

    return binary_search(list, target, start, end)


my_list =  [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
print(binary_search(my_list, 1, 0, len(my_list) - 1))