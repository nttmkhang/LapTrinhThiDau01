#cai tien lan 2

def GiaiThua(n):
    T = 1
    for i in range (1, n + 1):
        T *= i
    return T

def Catalan(n):
    a = GiaiThua(2 * n)
    b = GiaiThua(n)
    return a / b / b / (n + 1) 

def main():
    n = int(input("Nhap n: "))
    print("Catalan(n) = ", Catalan(n))

if __name__ == "__main__":
    main()

