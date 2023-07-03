
def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Muc 6.5.5.1

def TongChan(n) :
    s = 0
    for i in range(2, 2 * n + 1, 2) :
        s += i
    return s

def main() :
    n = Nhap()
    s = TongChan(n)
    print("Tong cac so chan tu 2 toi 2n:", s)
   

if __name__ == "__main__" :
    main()