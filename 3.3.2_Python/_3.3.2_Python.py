def countDivisors_2(n):
    T = 1
    p = 2
    while n > 1:
        count = 0
        while n % p == 0:
            count = count + 1
            n = n / p
        T = T * (count + 1)
        p = p + 1
    return T