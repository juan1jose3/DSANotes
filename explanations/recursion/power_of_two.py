def power_of_two(n):
    if n == 0:
        return 1
    
    pow = power_of_two(n-1)
    pow *= 2
    return pow


print(power_of_two(10))


