def sumDivisors_4(n):
    minprime = [i for i in range(n+1)]
    for p in range(2, int(n**0.5)+1):
        if minprime[p] == p:
            for i in range(p*p, n+1, p):
                if minprime[i] == i:
                    minprime[i] = p

    T = 1
    while n > 1:
        minp = minprime[n]
        count = 0
        power = 1
        while n % minp == 0:
            count += 1
            power *= minp
            n = n / minp
        T = T * (power * minp - 1) / (minp - 1)
    return T
