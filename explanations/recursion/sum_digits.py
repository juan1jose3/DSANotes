def sum_digits(number):
    pos_number = abs(number)
    if pos_number == 0:
        return 0
    
    last_digit = pos_number % 10
    return sum_digits(pos_number // 10) + last_digit




print(sum_digits(-451))

