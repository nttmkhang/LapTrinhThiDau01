
def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Mục 6.7, Bài tập 42

def Tong(n) :
    s = 1
    for i in range(1, n + 1) :
        if i % 2 != 0 :
            s = s - (3*i-1) + (3*i) - (3*i+1)
        else :
            s = s + (3*i-1) - (3*i) + (3*i+1)
    return s

def main() :
    n = Nhap()
    s = Tong(n)
    print("So hang thu n cua day so la:", s)
   

if __name__ == "__main__" :
    main()