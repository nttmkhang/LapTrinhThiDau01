def ktNguyenTo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Nhap n: "))
    if ktNguyenTo(n) == True:
        print("n la so nguyen to")
    else:
        print("n khong la so nguyen to")

if __name__ == "__main__":
    main()
