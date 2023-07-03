import math

def Nhap() :
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    return a, b

# Muc 3.5.2

def uscln_2(a, b) :
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0 :
        if a > b :
            a = a % b
        else : 
            b = b % a
    return a + b

def main() :
    a, b = Nhap()
    t = uscln_2(a, b)
    print("Uoc so chung lon nhat cua a va b la:", t)

if __name__ == "__main__" :
    main()