def Factorization(n):
    factorprime = []
    p = 2
    while n > 1:
        while n % p == 0:
            factorprime.append(p)
            n //= p
        p += 1
    return factorprime