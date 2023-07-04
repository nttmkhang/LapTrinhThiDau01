def modBigNum(x, y):
    kY = ["0"] * 11
    for i in range(1, 11):
        kY[k] = addBigNum(kY[k - 1], y)
    hold = ''
    for i in range(0, len(x)):
        hold = hold + x[i]
        k = 0
        while(compareBigNum(hold, kY[k + 1]) != -1):
            k += 1
        hold = subBigNum(hold, kY[k])
    return hold

