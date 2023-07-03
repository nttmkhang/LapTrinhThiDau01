def Catalan(n):
    a = BigFactorial(2 * n)
    b = BigFactorial(n)
    c = BigFactorial(n + 1)
    return divBigNum(divBigNum(a, b), c)
