def divBigNum(x, y):
    temp = ""
    hold = 0
    ss = 0
    for i in range(len(x)):
        hold = hold * 10 + int(x[i])
        ss = hold // y
        temp = temp + str(ss)
        hold = hold % y
    while(len(temp) > 1 and temp[0] == '0'):
        temp = temp[1:]
    return temp
