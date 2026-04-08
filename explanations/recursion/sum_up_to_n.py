def sum_up_to_n(n):
    if n == 1:
        return n
    
    return sum_up_to_n(n-1) + n




print(sum_up_to_n(10))