def sumDivisors_3(n):
    T = 1
    p = 2
    while (n > 1 and p * p <= n):
        count = 0
        power = 1
        while (n % p == 0):
            power *= p
            count += 1
            n //= p
        if (count > 0):
            T = T * (power * p - 1) // (p - 1)
        p += 1
    if (n > 1):
        T = T * (n * n - 1) // (n - 1)
    return T
