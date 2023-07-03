def ktNguyenTo(n):
    for i in range (2, n//2):
        if n % i == 0:
            return 0
    return n > 1

def main():
    n = int(input("Nhap n: "))
    if ktNguyenTo(n) == True:
        print("n la so nguyen to")
    else:
        print("n khong la so nguyen to")

if __name__ == "__main__":
    main()

