def isHappy(n:int):
    num = n
    sum_squares = set()
    total = 0
    while num != 1:
        total = 0 #this is very important
        while num > 0:
            digit = num % 10
            total += digit**2
            num //= 10

        num = total
        if total not in sum_squares:
            sum_squares.add(total)
        else: return False
        
    return True
      
print(isHappy(7))