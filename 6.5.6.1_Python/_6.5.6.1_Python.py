def TongBa(n):
    s = 0
    for i in range (2, 3 * n, 3):
        s += i
    return s

def main():
    n = int(input("Nhap n: "))

    print("Tong ba: ", TongBa(n))

if __name__ == "__main__":
    main()
