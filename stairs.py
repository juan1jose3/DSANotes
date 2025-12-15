import math
def climbStairs(n:int):
    """
        recursive approach
    
    
    if n == 0:
        return 1
    if n == 1 :
        return 1
    if n == 2:
        return 2
    
    return climbStairs(n-1) + climbStairs(n-2)
    """

    #Binet's approach

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
   

    sideA = (1+math.sqrt(5))/2
    sideB = (1-math.sqrt(5))/2
    binet = round((sideA**(n+1) - sideB**(n+1)) /math.sqrt(5))
    return  binet
        






print(climbStairs(1))