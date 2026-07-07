def reverse_list(list):
    
    if len(list) == 0:
        return []
    
    value_list = [list[0]]
    
    return reverse_list(list[1:]) + value_list


print(reverse_list(["a", "b", "c"]))