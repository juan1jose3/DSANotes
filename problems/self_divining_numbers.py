def selfDividingNumbers(left, right):
    nums = []
    for i in range(left,right + 1):
        
        n = i
        digit_size = len(str(n))
        if n < 10:
            nums.append(n)
        elif n > 10:
            digitNum = 0
            while n > 0:
                last_digit = n % 10
                
                if last_digit != 0 and i % last_digit  == 0:
                    digitNum+=1
                n //= 10
            
            if digitNum == digit_size:
                nums.append(i)
                
    
    return nums


        



print(selfDividingNumbers(47,85))