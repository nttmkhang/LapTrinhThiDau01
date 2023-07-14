def BigFactorial(n):
    T = "1"
    for i in range (1, n + 1):
        T = mulBigNum(T, i)
    return T
