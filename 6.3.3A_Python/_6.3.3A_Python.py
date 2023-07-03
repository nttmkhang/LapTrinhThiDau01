def LuyThua(x, n):
    t = 1
    while(n > 0):
        if(n % 2 != 0):
            t = t * x
        x = x * x
        n = n // 2
    return t