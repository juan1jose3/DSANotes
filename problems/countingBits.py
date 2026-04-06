def countBits(n:int):
    count = []
    count.append(0)
    for number in range(1,n+1):
        counter = 0
        current = number
         
        while current > 0: 
            
            lastDigit = current % 2
            if lastDigit == 1:
                counter += 1

            current = current // 2
            
            
        count.append(counter)


                




            
    return count


print(countBits(8))