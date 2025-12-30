def reverseVowels(s):
    vowelSack = []
    vowels = "aeiouAEIOU"
    newStr = ""
    for i in s:
        if i in vowels:
            vowelSack.append(i)
    
    
    for j in s:
        if j in vowels:
            newStr += vowelSack[-1]
            vowelSack.pop()
           
        else:
            newStr += j
    return newStr









print(reverseVowels("IceCreAm"))