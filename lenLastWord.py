def lengthOfLastWord(str:str):
    fullStr = str.strip(" ")

    splitedStr = fullStr.split()

    return len(splitedStr[len(splitedStr)-1])



print(lengthOfLastWord("Hello World"))