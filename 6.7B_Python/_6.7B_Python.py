

def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Mục 6.7, Bài tập 42, Hàm cài đặt Vicky

def Tong(n) :
    s = 0
    for i in range(1, 3 * n + 2) :
        if i % 2 != 0 :
            s += i
        else :
            s -= i
    return s

def main() :
    n = Nhap()
    s = Tong(n)
    print("So hang thu n cua day so la:", s)
   

if __name__ == "__main__" :
    main()