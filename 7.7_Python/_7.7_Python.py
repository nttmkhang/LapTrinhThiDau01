class BigNum(str) :
    pass

def toNumber(c):
    if c == '0':
        return 0
    if c == '1':
        return 1
    if c == '2':
        return 2
    if c == '3':
        return 3
    if c == '4':
        return 4
    if c == '5':
        return 5
    if c == '6':
        return 6
    if c == '7':
        return 7
    if c == '8':
        return 8
    if c == '9':
        return 9
    if (c == 'A') or (c == 'a'):
        return 10
    if (c == 'B') or (c == 'b'):
        return 11
    if (c == 'C') or (c == 'c'):
        return 12
    if (c == 'D') or (c == 'D'):
        return 13
    if (c == 'E') or (c == 'e'):
        return 14
    return 15

def mulBigNum(x, y):
    temp = ""
    zero = ""
    for i in range (len(x) - 1, 0, -1):
        xx = toNumber(x[i])
        ss = mulBigNum(y, xx)
        ss = ss + zero
        temp = addBigNum(temp, ss)
        zero = zero + '0'
    return temp
