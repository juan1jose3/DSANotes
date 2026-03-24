def getPrefix(strs):
    strs.sort()

    if len(strs) < 2:
        return strs[0]
        
    initialPrefix = ""
    endPrefix = ""
    longest = ""
    for i in range(0,len(strs[0])):

        initialPrefix = strs[0][i]
        endPrefix = strs[len(strs)-1][i]

        if initialPrefix == endPrefix:
            longest += initialPrefix
        
        else:
            break
        
    if longest == "":
        return ""
    else:
        return longest

    
    

        
           
        
    
print(getPrefix(["flower","flow","flight"]))
        