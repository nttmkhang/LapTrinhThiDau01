#cai tien lan 1

def GiaiThua(n):
    T = 1
    for i in range (1, n + 1):
        T *= i
    return T

def Catalan(n):
    a = GiaiThua(2 * n)
    b = GiaiThua(n)
    c = GiaiThua(n + 1)
    return a / b / c

def main():
    n = int(input("Nhap n: "))
    print("Catalan(n) = ", Catalan(n))

if __name__ == "__main__":
    main()
