def is_sorted(list):
 
    if len(list) == 1 or len(list) == 0:
        return True
    
    sorted_status = is_sorted(list[1:]) 

    return list[0] <= list[1] and sorted_status
    
    

print(is_sorted([1, 2, 3, 3, 2]))