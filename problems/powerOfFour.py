import math
def powerOfFour(n:int):
    if n > 0:
        log = round(math.log(n,4))
        if 4 ** log == n:
            return True
    return False
    


print(powerOfFour(2))