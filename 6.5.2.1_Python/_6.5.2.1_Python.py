def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Muc 6.5.2.1

def TongBinhPhuong(n) : 
    s = 0
    for i in range(1, n + 1) :
        s += i * i
    return s

def main() :
    n = Nhap()
    s = TongBinhPhuong(n)
    print("Tong binh phuong cac so tu 1 toi n:", s)
   

if __name__ == "__main__" :
    main()
