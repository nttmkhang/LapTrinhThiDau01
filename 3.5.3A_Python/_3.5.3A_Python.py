def Nhap():
    n = int(input("Nhap mot so: "))
    return n

def uscln_3(a, b):
    a = abs(a)
    b = abs(b)
    while a != 0 and b != 0:
        a = a % b
        a, b = b, a
    return a + b

def main():
    a = Nhap()
    b = Nhap()
    print("Uoc so chung lon nhat cua a va b la", uscln_3(a, b))

if __name__ == "__main__":
    main()