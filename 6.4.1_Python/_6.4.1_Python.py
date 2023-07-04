def powerModulo(a, b, M):
    t = 1
    while b > 0:
        if b % 2 == 1:
            t = t * a
        b = b // 2
        a = a * a
    return t % M
