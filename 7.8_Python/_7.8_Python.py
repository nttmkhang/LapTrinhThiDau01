def divBigNum(x, y):
    temp = ""
    hold = 0
    ss = 0
    for i in range (0, len(x)):
        hold = hold * 10 + toNumber(x[i])
        ss = hold / y
        temp = temp + toChar(ss)
        hold = hold % y
    while len(temp) > 1 and temp[0] == '0':
        temp.erase(0, 1)
    return temp
