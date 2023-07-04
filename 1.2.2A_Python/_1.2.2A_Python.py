def DecimalToBinary_1(n):
    temp = ""
    while n > 0:
        if n % 2 != 0:
            temp = "1" + temp
        else:
            temp = "0" + temp
        n = n // 2
    return temp
