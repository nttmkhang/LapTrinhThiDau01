def countDivisor_3(n):
    T = 1
    p = 2
    while(n > 1 and p * p <= n):
        count = 0
        while(n % p == 0):
            count += 1
            n = n // p
        T = T * (count + 1)
        p = p + 1
    if(n > 1):
        T = T * 2
    return T