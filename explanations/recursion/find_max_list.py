def find_max(list):

    if len(list) == 1:
        return list[0]
    
    return find_max(list[1:])


print(find_max([[3, 7, 2, 9, 4]]))