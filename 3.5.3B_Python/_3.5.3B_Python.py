def Nhap():
    n = int(input("Nhap n: "))
    return n

def uscln(a, b):
    a = abs(a)
    b = abs(b)
    while b > 0:
        a = a % b
        a, b = b, a
    return a

def main():
    a = Nhap()
    b = Nhap()
    print("Uoc so chung lon nhat cua a va b la", uscln(a, b))

if __name__ == "__main__":
    main()