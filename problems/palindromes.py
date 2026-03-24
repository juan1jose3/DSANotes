def findPalindrome(s):
    reversedStr = ""
    for i in s:
        if i.isalnum():
            reversedStr +=i.lower()
    return reversedStr == reversedStr[::-1]

print(findPalindrome("Was it a car or a cat I saw?"))