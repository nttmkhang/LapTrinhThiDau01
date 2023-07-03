def divBigNum(x, y):
    kY = ["0"] * (11)
    for k in range(1, 11):
        kY[k] = addBigNum(kY[k - 1], y)

    temp = ""
    hold = ""
    for i in range(len(x)):
        hold = hold + x[i]
        k = 0
        while compareBigNum(hold, kY[k + 1]) != -1:
            k += 1
        temp = temp + toChar(k)
        hold = subBigNum(hold, kY[k])

    while len(temp) > 1 and temp[0] == '0':
        temp = temp[1:]

    return temp
