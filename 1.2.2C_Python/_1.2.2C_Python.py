def DecimalToBinary_3(n):
    temp = ""
    while n:
        if n & 1:
            temp = "1" + temp
        else:
            temp = "0" + temp
        n >>= 1
    return temp
