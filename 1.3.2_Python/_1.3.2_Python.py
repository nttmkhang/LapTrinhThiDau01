def Nhap() :
    n = int(input("Nhap n: "))
    return n;

def toChar(n) :
    Letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return Letter[n]

def DecimalToHexa(n) :
    temp = ""
    while n > 0 : 
        temp += toChar(n % 16)
        n = int(n / 16)
    return temp

def main() :
    n = Nhap()
    S = DecimalToHexa(n)
    print("Dang Hexa cua n:",S)
   

if __name__ == "__main__" :
    main()
