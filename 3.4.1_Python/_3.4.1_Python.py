def Nhap():
    n = int(input("Nhap n: "))
    return n

def sumDivisors_1(n):
    s = 0
    for i in range (1, n + 1):
        if (n % i == 0):
            s = s + i
    return s

def main():
    n = Nhap()
    print("Tong cac uoc so cua n la ", sumDivisors_1(n))

if __name__ == "__main__":
    main()