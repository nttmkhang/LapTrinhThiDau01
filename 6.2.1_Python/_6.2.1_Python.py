def mulEgyptModulo(a, b, M):
    t = 0
    while b >= 1:
        if b % 2 != 0:
            t = (t % M + a % M) % M
        b = b // 2
        a = a * 2
    return t