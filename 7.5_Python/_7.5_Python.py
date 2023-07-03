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

def toChar(n):
    Letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return Letter[n]

def subBigNum(x, y):
    while(len(x) < len(y)): x = '0' + x
    while(len(y) < len(x)): y = '0' + y
    borrow = 0
    temp = ''
    for i in range(len(x) - 1, -1, -1):
        xx = toNumber(x[i])
        yy = toNumber(y[i])
        ss = xx - yy - borrow
        if(ss < 0):
            ss += 10
            borrow = 1
        else:
            borrow = 0
        temp = toChar(ss) + temp
    while(len(temp) > 1 and temp[0] == '0'):
        temp = temp[1:]
    return temp