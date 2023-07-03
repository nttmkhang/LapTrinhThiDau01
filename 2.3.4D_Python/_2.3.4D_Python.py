def ktNguyenTo(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    n = int(input('Nhap n: '))
    if ktNguyenTo(n):
        print(n, 'la so nguyen to!!!')
    else:
        print(n, 'khong la so nguyen to!!!')
    print('\n\n\nKet thuc!!!!')

if __name__ == "__main__":
    main()