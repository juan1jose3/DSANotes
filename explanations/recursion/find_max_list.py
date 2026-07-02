def find_max(list):
    if len(list) == 0:
        return None
    
    if len(list) == 1:
        return list[0]
    
    sliced = find_max(list[1:]) 
    
    if list[0] > sliced:
        return list[0]
    else:
        return sliced


print(find_max([3, 7, 2, 9, 4]))