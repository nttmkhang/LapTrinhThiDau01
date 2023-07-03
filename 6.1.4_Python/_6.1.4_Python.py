def Nhap() :
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    return a, b

# Muc 6.1.4

def mulEgypt(a, b) : 
    if b == 0 : 
        return 0
    t = mulEgypt(a, int(b / 2)) 
    if b % 2 != 0 :
        return t + t + a
    return t + t

def main() :
    a, b = Nhap()
    s = mulEgypt(a, b)
    print("Ket qua cua a nhan b la:", s) 

if __name__ == "__main__" :
    main()
