def Nhap():
    n = int(input("Nhap n: "))
    return n

def ktNguyenTo(n):
    dem = 0
    for i in range (1, n + 1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        return True
    return False

def main():
    n = Nhap()
    if ktNguyenTo(n):
        print("n la so nguyen to")
    else:
        print("n khong la so nguyen to")

    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()