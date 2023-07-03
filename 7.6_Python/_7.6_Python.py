
def Nhap() :
    a = str(input("Nhap so nguyen lon a: "))
    b = int(input("Nhap so nguyen nho b: "))
    return a, b

# Muc 7.6

def mulBigNum(x, y) :
    carry = 0
    temp = ""
    for i in range(len(x)-1, -1, -1) :
        xx = int(x[i])
        ss = xx * y + carry
        temp = str(ss % 10) + temp
        carry = int (ss / 10)
    if carry > 0 :
        temp = str(carry) + temp
    return temp


def main() :
    a, b = Nhap()
    s = mulBigNum(a, b)
    print("Tich cua a va b la:", s)
   

if __name__ == "__main__" :
    main()