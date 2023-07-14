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

def DecimalToBinary(n):
    temp = ""
    while n > 0:
        if n % 2 != 0:
            temp = "1" + temp
        else:
            temp = "0" + temp
        n = n // 2
    return temp

def HexaToBinary(n):
    temp = ''
    for i in range (0, len(n)):
        index = toNumber(n[i])
        group = DecimalToBinary(index)
        while (len(group) < 4):
            group = '0' + group
        temp = temp + group
    while (len(temp) > 1 and temp[0] == '0'):
        temp = temp[1:]
    return temp

def main():
    sHexa = input('Nhap chuoi thap luc phan: ')

    print("Bieu dien chuoi thap luc phan ", sHexa, "o he co so 2 la: ",HexaToBinary(sHexa))

    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()