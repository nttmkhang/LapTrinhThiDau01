def sumDivisors_2(n):
    T = 1
    p = 2
    while n > 1:
        count = 0
        power = 1
        while n % p == 0:
            power *= p
            count += 1
            n /= p
        T = T * (power * p - 1) / (p - 1)
        p += 1
    return T