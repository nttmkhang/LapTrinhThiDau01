
# Muc 7.12, Bai tap 44

class BigNum(str) :
    pass

def Nhap() :
    n = int(input("Nhap n: "))
    return n

def BigFibonacci(n) :
    Ftt = "1"
    Ft = "1"
    i = 2
    Fhh = "1"
    while i < n :
        Fhh = addBigNum(Ft, Ftt)
        i+=1
        Ftt = Ft
        Ft = Fhh
    return Fhh

def addBigNum(x, y) :
    while(len(x) < len(y)) :
        x = "0" + x
    while(len(x) > len(y)) :
        y = "0" + y

    carry = 0
    temp = ""
    for i in range(len(x)-1, -1, -1) :
        xx = int(x[i])
        yy = int(y[i])
        ss = xx + yy + carry

        temp = str(ss % 10) + temp
        carry = int(ss/10)
    if carry > 0 :
        temp = "1" + temp
    return temp

def main() :
    n = Nhap()
    print("So hang fibo thu",n,":",BigFibonacci(n))
    print("Ket thuc!!!!")

if __name__ == "__main__":
    main()