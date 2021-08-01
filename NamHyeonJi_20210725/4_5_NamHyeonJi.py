def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        res = False 
    else:
        while n % 4 == 0: 
            n = n / 4 
        if n == 1: 
            res = True 
        else: 
            res = False 
    return res

print(isPowerOfFour(16))


    

