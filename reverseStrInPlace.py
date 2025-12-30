def reverseStr(s:list[str]):

# this is called the two-pointer approach
# this problem is the exact same as reversing a list
    
    end = len(s) - 1

    for start in range(len(s)):

        if  start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
        end -= 1
            
    return s







print(reverseStr(["H","a","n","n","a","h"]))