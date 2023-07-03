def BinaryToDecimal(n):
    reversed_n = n[::-1]
    temp = 0
    twopower = 1
    for i in range (0, len(reversed_n)):
        temp = temp + twopower * int(reversed_n[i])
        twopower *= 2
    return temp