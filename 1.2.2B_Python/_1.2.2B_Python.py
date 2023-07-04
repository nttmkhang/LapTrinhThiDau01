def DecimalToBinary_2(n):
    temp = ""
    while n > 0:
        temp = str(n % 2) + temp
        n //= 2
    return temp