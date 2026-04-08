def list_crusher(list):
    size = len(list) - 1

    if size < 0:
        return 0

    if size == 0:
        return list[size]
    
    element = list[size]
    list.pop(size)

    element += list_crusher(list)

    return  element
    

    

print(list_crusher([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
ALTERNATIVE

def list_crusher(lst):
    if not lst: # Base case: list is empty
        return 0
    return lst[0] + list_crusher(lst[1:]) # Head + Recurse on Tail
"""

