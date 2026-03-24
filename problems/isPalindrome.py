def isPalindrome(s):
    newStr = ""
    for i in s.strip().lower():
        if i.isalnum():
            newStr +=i
    print(newStr)
    print(newStr[::1])
    return newStr == newStr[::-1]


print(isPalindrome("race a car"))