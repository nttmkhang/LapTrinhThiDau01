def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    Ftt = 0
    Ft = 1
    i = 2
    Fhh = 0
    while(i <= n):
        Fhh = Ft + Ftt
        i += 1
        Ftt = Ft
        Ft = Fhh
    return Fhh