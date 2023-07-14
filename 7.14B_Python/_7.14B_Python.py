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

def addBigNum(x, y):
    while len(x) < len(y):
        x = '0' + x
    while len(x) > len(y):
        y = '0' + y
    
    carry = 0
    temp = ""
    for i in range(len(x) - 1, -1, -1):
        xx = toNumber(x[i])
        yy = toNumber(y[i])
        ss = xx + yy + carry
        
        temp = str(ss % 10) + temp
        carry = ss // 10
    
    if carry > 0:
        temp = "1" + temp
    return temp

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

def BigFactorial(n):
    T = "1"
    for i in range (1, n + 1):
        T = mulBigNum(T, i)
    return T

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

def BigCatalan(n):
    a = BigFactorial(2 * n)
    b = BigFactorial(n)
    c = BigFactorial(n + 1)
    return divBigNum(divBigNum(a, b), c)

def main():
    n = int(input("Nhap n: "))
    print("So hang catalan ", n)
    print("! : ", BigCatalan(n))
    print("\n\n\nKet Thuc!!!!")

if __name__ == "__main__":
    main()