def powerModulo(a, b, M):
    if (b == 0):
        return 1
    t = powerModulo(a, b // 2, M) % M
    t = mulEgyptModulo(t, t, M)
    if (b % 2 == 0):
        return t
    return mulEgyptModulo(t, a, M)