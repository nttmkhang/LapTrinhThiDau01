def Factorization(n):
    factorprime = []
    p = 2
    while n > 1 and p * p <= n:
        while n % p == 0:
            factorprime.append(p)
            n //= p
        p += 1
    if n > 1:
        factorprime.append(n)
    return factorprime
