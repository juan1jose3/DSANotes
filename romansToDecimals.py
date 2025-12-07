def romansToDecimals(s):
    symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    
    number = 0
    
    size = len(s) -1
    for i in range(size):
        currentNumber = symbols[s[i]]
        currentNumberPlus = symbols[s[i+1]]
        if currentNumber < currentNumberPlus:
             number -= currentNumber # Roman numerals are single digits not pairs IV is not a pair is I V
        else:
       
            number += symbols[s[i]]
    return number + symbols[s[size]]




print(romansToDecimals("XIV"))