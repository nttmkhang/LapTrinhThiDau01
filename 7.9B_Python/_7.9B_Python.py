def modBigNum(x, y):
    hold = 0
    for i in range(len(x)):
        hold = hold * 10 + int(x[i])
        hold = hold % y
    return hold
