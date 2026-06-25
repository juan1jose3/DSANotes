def list_sum(list):
    size = len(list) - 1


    if size < 0:
        return 0

    counter = list[size]
    return counter + list_sum(list[:size]) 


    

print(list_sum([1, 2, 3, 4]))