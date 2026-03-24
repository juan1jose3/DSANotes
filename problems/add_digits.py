def addDigits(num:int):
    number = num
    adding = 0

    while number >= 10:
        adding = 0

        while number > 0:
            digit = number % 10
            
            number //=10
            adding += digit
        number = adding
        


        
    return number


print(addDigits(1))