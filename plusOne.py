def plusOne(digits:list[int]):
    lastDigit = len(digits) -1

    if digits[lastDigit] == 9:

        while lastDigit > 0:
            carry = 1
            if digits[lastDigit] != 9:
                digits[lastDigit] += carry
                return digits

            digits[lastDigit] = 0

            lastDigit -= 1
        if digits[lastDigit] == 9:
            digits.append(0)
            digits[lastDigit] = 1

        elif digits[lastDigit]!=9:
            digits[lastDigit] += 1

    else:
        digits[lastDigit] = digits[lastDigit] + 1
    return digits


   
     





print(plusOne([9]))