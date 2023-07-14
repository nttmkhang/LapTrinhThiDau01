def TongLapPhuong(n):
    s = 0
    for i in range (1, n + 1):
        s = s + i * i * i
    return s

def main():
    n = int(input("Nhap n: "))

    print("Tong lap phuong cua n la: ", TongLapPhuong(n))

if __name__ == "__main__":
    main()
