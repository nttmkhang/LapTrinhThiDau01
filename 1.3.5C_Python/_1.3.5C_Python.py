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

def HexaToBinary_3(n):
    hexbinary = {'0':"0000",'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110",'7':"0111",'8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
    temp = ''
    for i in range (0, len(n)):
        temp += hexbinary[n[i].upper()]
    while (len(temp) > 1 and temp[0] == '0'):
        temp = temp[1:]
    return temp

def main():
    sHexa = input('Nhap chuoi thap luc phan: ')

    print("Bieu dien chuoi thap luc phan ", sHexa, "o he co so 2 la: ",HexaToBinary_3(sHexa))

    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()
