def getPrefix(strs):
    counter = 0
        
    prefix = ""
    if strs[0]:
        first_item = strs[0]
        size = len(first_item)
        if size > 1:
            size = 2
        else:
            return first_item
        for i in range(size):
            prefix += first_item[i]
    else:
        return ""
        
    for i in strs:
        if i.startswith(prefix):
            counter += 1
        if counter > 1:
            return prefix
    return ""
    
print(getPrefix(["flower","flow","flight"]))
        