def HexaToDecimal(n):
    temp = 0
    for i in range(len(n)):
        temp *= 16
        temp += int(n[i], 16)
    return temp
