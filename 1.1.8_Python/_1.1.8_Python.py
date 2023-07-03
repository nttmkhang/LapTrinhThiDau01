def Nhap() :
    n = int(input("Nhap n: "))
    return n;

def toChar(n) :
    Letter = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return Letter[n]

def main() :
    n = Nhap()
    print(toChar(n))

if __name__ == "__main__" :
    main()